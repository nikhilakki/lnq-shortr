# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Union
from pydantic import AnyHttpUrl, BaseSettings, Field


class Settings(BaseSettings):
    CORS_ORIGINS: list[Union[str, AnyHttpUrl]] = [
        "http://localhost:8000",
        "http://localhost:3000",
    ]
    DOMAIN: str = Field(default="http://localhost:8000", env="DOMAIN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
