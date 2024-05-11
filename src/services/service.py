from functools import lru_cache
from typing import Type


from core.config import settings
from core.logger import logger
from schemas.models import Output
from schemas.structs import MsgOutput




@lru_cache()
def get_some_service() -> Type["SomeService"]:
    return SomeService


class SomeService:
    @staticmethod
    async def send(event: str, x_request_id: str) -> Output:
        if settings.some_setting:
            logger.info(f"get event {event} via request {x_request_id}")
        return Output(res=42)

    # @log_info
    async def receive(event: str, x_request_id: str):
        res = MsgOutput(res=42)
        logger.info(f"return result {res.encode()} for request {x_request_id}")
        return res.encode()
