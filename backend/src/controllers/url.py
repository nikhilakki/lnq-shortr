# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter
from src.services import url, GenerateShortURL

router = APIRouter()


@router.post("/short-url", status_code=201)
async def shorten_url(generateShortURL: GenerateShortURL):
    return await url.shorten_url(generateShortURL, generateShortURL.user_id)


@router.get("/short-url/all", status_code=200)
async def get_url_all():
    return await url.get_url_all()


@router.delete("/short-url/{id}")
async def delete_url(id: int):
    return await url.delete_url(id)


@router.get("/{short_url}")
async def short_to_big_url(short_url: str):
    return await url.short_to_big_url(short_url)
