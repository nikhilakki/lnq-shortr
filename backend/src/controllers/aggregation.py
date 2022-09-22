# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""
Aggregation layer
"""

from fastapi import APIRouter, Security
from src.utils.logger import logging
from src.services import user, quota, url, GenerateShortURL
from src import azure_scheme

router = APIRouter()


@router.post("/aggregation/short-url", dependencies=[Security(azure_scheme)])
async def generateShortUrl(
    generateShortURL: GenerateShortURL,
):
    """
    Step - 1: Generate short url
    """
    logging.debug(f"{user=}")
    res = await url.shorten_url(generateShortURL)
    logging.debug(res)
    return res
