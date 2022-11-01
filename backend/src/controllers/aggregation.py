# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""
Aggregation layer
"""

from fastapi import APIRouter
from src.utils.logger import logging
from src.services import user, url, GenerateShortURL

router = APIRouter()


@router.post("/aggregation/short-url")
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
