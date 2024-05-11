import os
from pydantic_settings import BaseSettings


class TestSettings(BaseSettings):
    app_host: str = "test_api"
    app_port: str = "8000"

    endpoint: str = "some_api/v1"
    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


settings = TestSettings(_env_file="../.env")
