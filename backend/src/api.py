# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


from fastapi import FastAPI
from src.models import database
from fastapi.middleware.cors import CORSMiddleware

from src.controllers import (
    url_router,
    user_router,
    quota_router,
    aggregation_router,
    auth_router,
)

from src.utils.logger import logger as logging
from . import settings

app = FastAPI()

app.include_router(url_router, tags=["URL API"])
app.include_router(user_router, tags=["User API"])
app.include_router(quota_router, tags=["Quota API"])
app.include_router(aggregation_router, tags=["Aggregation API"])
app.include_router(auth_router, tags=["Auth API"])


if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/config/all")
def return_config():
    logging.debug(f"{settings}")
    return settings.dict()


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
