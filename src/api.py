# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
from typing import Union
from fastapi import FastAPI, Security
from src.models import database
from pydantic import AnyHttpUrl, BaseSettings, Field
from fastapi.middleware.cors import CORSMiddleware
from fastapi_azure_auth import MultiTenantAzureAuthorizationCodeBearer
from src.routes import router as url_shortr_router
from src.logger import logger as logging


class Settings(BaseSettings):
    SECRET_KEY: str = Field("my super secret key", env="SECRET_KEY")
    BACKEND_CORS_ORIGINS: list[Union[str, AnyHttpUrl]] = ["http://localhost:8000"]
    OPENAPI_CLIENT_ID: str = Field(default="", env="OPENAPI_CLIENT_ID")
    APP_CLIENT_ID: str = Field(default="", env="APP_CLIENT_ID")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

app = FastAPI(
    swagger_ui_oauth2_redirect_url="/oauth2-redirect",
    swagger_ui_init_oauth={
        "usePkceWithAuthorizationCodeGrant": True,
        "clientId": settings.OPENAPI_CLIENT_ID,
    },
)
app.include_router(url_shortr_router)
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


azure_scheme = MultiTenantAzureAuthorizationCodeBearer(
    app_client_id=settings.APP_CLIENT_ID,
    scopes={
        f"api://{settings.APP_CLIENT_ID}/user_impersonation": "user_impersonation",
    },
    validate_iss=False,
)


@app.on_event("startup")
async def load_config() -> None:
    """
    Load OpenID config on startup.
    """
    logging.info("On event - Startup...")
    await azure_scheme.openid_config.load_config()
    await database.connect()
    logging.info("On event - Startup Complete!")


@app.on_event("shutdown")
async def shutdown():
    logging.info("On event - Shutdown...")
    await database.disconnect()
    logging.info("On event - Shutdown Complete!")


@app.get("/")
async def health_check():
    return {"response": "Health check success"}
