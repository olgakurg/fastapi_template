from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status, Request
from services.service import SomeService, get_some_service

router = APIRouter()


@router.get(
    "/pydantic",
    status_code=status.HTTP_200_OK,
    summary="Ручка для чего-то",
    description="особенности ручки",
    tags=["GET"],
)
async def get_pydantic(
    request: Request,
    payload: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern=r"\d+")
    ] = None,
    some_service: SomeService = Depends(get_some_service),
):
    if payload:
        res = await some_service.send(
            event=payload, x_request_id=request.headers["X-Request-Id"]
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Invalid payload"
        )

    return res


@router.get(
    "/msgspec",
    status_code=status.HTTP_200_OK,
    summary="Ручка для чего-то",
    description="особенности ручки",
    tags=["GET"],
)
async def get_msgspec(
    request: Request,
    payload: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern=r"\d+")
    ] = None,
    some_service: SomeService = Depends(get_some_service),
):
    if payload:
        res = await some_service.receive(
            event=payload, x_request_id=request.headers["X-Request-Id"]
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Invalid payload"
        )

    return res
