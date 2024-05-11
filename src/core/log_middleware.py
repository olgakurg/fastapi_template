from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from .logger import logger


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = await call_next(request)
        logger.info(
            "Incoming request",
            extra={
                "req": {
                    "method": request.method,
                    "url": str(request.url),
                    "x_request_id": str(request.headers["X-Request-Id"]),
                },
                "res": {"status_code": response.status_code},
            },
        )
        return response
