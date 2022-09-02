# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter, Security
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from src.hash import generate_url_hash
from src.models import database, urls_table

router = APIRouter()


class GenerateShortURL(BaseModel):
    url: str


@router.post("/short-url")  # , dependencies=[Security(azure_scheme)])
async def shortended_url(generateShortURL: GenerateShortURL):
    url = generateShortURL.url
    short_url = generate_url_hash()
    query = urls_table.insert().values(url=url, short_url=short_url)
    record_id = await database.execute(query)
    return {"response": dict(url=url, short_url=short_url, record_id=record_id)}


@router.get("/short-url/all")  # , dependencies=[Security(azure_scheme)])
async def all_records():
    query = urls_table.select()
    return await database.fetch_all(query)


@router.get("/{short_url}")
async def short_to_big_url(short_url: str):
    query = urls_table.select().where(urls_table.c.short_url == short_url)
    record = await database.fetch_one(query)
    url = record[-2]
    return RedirectResponse(url)
