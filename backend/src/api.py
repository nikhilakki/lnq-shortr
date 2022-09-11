# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Union
from fastapi import FastAPI
from src.models import database
from pydantic import AnyHttpUrl, BaseSettings, Field
from fastapi.middleware.cors import CORSMiddleware
from src.controllers import url_router, user_router, quota_router
from src.utils.logger import logger as logging


class Settings(BaseSettings):
    SECRET_KEY: str = Field("my super secret key", env="SECRET_KEY")
    CORS_ORIGINS: list[Union[str, AnyHttpUrl]] = [
        "http://localhost:8000",
        "http://localhost:3000",
    ]
    OPENAPI_CLIENT_ID: str = Field(default="", env="OPENAPI_CLIENT_ID")
    APP_CLIENT_ID: str = Field(default="", env="APP_CLIENT_ID")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

app = FastAPI()
app.include_router(url_router, tags=["URL Routes"])
app.include_router(user_router, tags=["User Routes"])
app.include_router(quota_router, tags=["Quota Routes"])

if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def load_config() -> None:
    """
    Load OpenID config on startup.
    """
    logging.info("On event - Startup...")
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
