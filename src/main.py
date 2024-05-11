from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from fastapi.responses import ORJSONResponse
from api.v1 import some
from core.config import settings
from core.log_middleware import LogMiddleware
from core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("lifespan starts")
    yield
    logger.info("lifespan finish")


app = FastAPI(
    title=settings.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


@app.middleware("http")
async def request_middleware(request, call_next):
    request_id = request.headers.get("X-Request-Id")
    if not request_id:
        return ORJSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "X-Request-Id is required"},
        )
    return await call_next(request)


app.add_middleware(LogMiddleware)

app.include_router(some.router, prefix="/some_api/v1")
