# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Union
from pydantic import AnyHttpUrl, BaseSettings, Field
from fastapi_azure_auth import MultiTenantAzureAuthorizationCodeBearer


class Settings(BaseSettings):
    CORS_ORIGINS: list[Union[str, AnyHttpUrl]] = [
        "http://localhost:8000",
        "http://localhost:3000",
    ]
    DOMAIN: str = Field(default="http://localhost:8000", env="DOMAIN")
    OPENAPI_CLIENT_ID: str = Field(default="", env="OPENAPI_CLIENT_ID")
    APP_CLIENT_ID: str = Field(default="", env="APP_CLIENT_ID")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

azure_scheme = MultiTenantAzureAuthorizationCodeBearer(
    app_client_id=settings.APP_CLIENT_ID,
    scopes={
        f"api://{settings.APP_CLIENT_ID}/user_impersonation": "user_impersonation",
    },
    validate_iss=False,
)
