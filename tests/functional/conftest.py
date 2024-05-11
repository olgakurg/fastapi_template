import asyncio
import pytest_asyncio
import httpx
from tests.functional.src.settings import settings


@pytest_asyncio.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def client():
    client = httpx.AsyncClient()
    yield client
    await client.aclose()


@pytest_asyncio.fixture
def make_request(client: httpx.AsyncClient()):
    async def inner(
        method: str,
        endpoint: str,
        params: dict = {},
        json: dict = {},
        headers: dict = {},
    ):
        headers["X-Request-Id"] = "test x-request-id"
        return await client.request(
            method,
            f"http://{settings.app_host}:{settings.app_port}/{endpoint}",
            params=params,
            json=json,
            headers=headers,
        )

    return inner
