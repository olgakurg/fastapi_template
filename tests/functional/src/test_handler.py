from http import HTTPStatus

import pytest

from settings import settings

pytestmark = pytest.mark.asyncio


@pytest.mark.xfail()
async def test_msgspec(make_request):
    handler = "msgspec"
    response = await make_request(
        method="GET",
        endpoint=f"{settings.endpoint}/{handler}",
        params={"payload": 1234},
    )
    assert response.status_code == HTTPStatus.OK


@pytest.mark.xfail()
async def test_pydantic(make_request):
    handler = "pydantic"
    response = await make_request(
        method="GET",
        endpoint=f"{settings.endpoint}/{handler}",
        params={"payload": 1234},
    )
    assert response.status_code == HTTPStatus.OK
