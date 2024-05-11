import pytest_asyncio
import os
import sys

project_path = os.path.abspath(os.path.join("../.."))

if project_path not in sys.path:
    sys.path.insert(0, project_path)


from services.service import SomeService


@pytest_asyncio.fixture(scope="function")
def make_service():
    return SomeService()
