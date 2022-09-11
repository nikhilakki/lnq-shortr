# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter
from src.services import url, GenerateShortURL

router = APIRouter()


@router.post("/short-url", status_code=201)
async def shortended_url(generateShortURL: GenerateShortURL):
    return await url.shortended_url(generateShortURL)


@router.get("/short-url/all", status_code=200)
async def all_records():
    return await url.all_records()


@router.delete("/short-url/{id}")
async def delete_record(id: int):
    return await url.delete_record(id)


@router.get("/{short_url}")
async def short_to_big_url(short_url: str):
    return await url.short_to_big_url(short_url)
