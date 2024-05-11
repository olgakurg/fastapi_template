import os
import sys
project_path = os.path.abspath(os.path.join("../.."))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

import pytest
from services.service import SomeService
from schemas.models import Output


@pytest.mark.xfail()
@pytest.mark.asyncio
async def test_send():
    service = SomeService()
    res = await service.send(event="some", x_request_id="none")
    assert res == Output(res=42)


@pytest.mark.xfail()
@pytest.mark.asyncio
async def test_receive(make_service):
    service = SomeService()
    res = await service.receive(x_request_id="any")
    assert res == b'{"res":42}'
