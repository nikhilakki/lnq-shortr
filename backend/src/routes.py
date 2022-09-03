# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from os import stat
from fastapi import APIRouter, Security
from fastapi.responses import RedirectResponse, Response
from pydantic import BaseModel
import validators
from validators.utils import ValidationFailure

from src.hash import generate_url_hash
from src.models import database, urls_table
from src.logger import logger as logging

router = APIRouter()


class GenerateShortURL(BaseModel):
    name: str = None
    url: str


@router.post("/short-url")  # , dependencies=[Security(azure_scheme)])
async def shortended_url(generateShortURL: GenerateShortURL):
    url = generateShortURL.url
    name = generateShortURL.name

    validation = validators.url(url)
    if validation:
        short_url = generate_url_hash()
        query = urls_table.insert().values(name=name, url=url, short_url=short_url)
        record_id = await database.execute(query)
        return {"response": dict(url=url, short_url=short_url, record_id=record_id)}
    else:
        return Response(status_code=400, content="Url not valid")


@router.get("/short-url/all")  # , dependencies=[Security(azure_scheme)])
async def all_records():
    query = urls_table.select()
    return await database.fetch_all(query)


@router.delete("/short-url/{id}")  # , dependencies=[Security(azure_scheme)])
async def delete_record(id: int):
    try:
        query = urls_table.delete().where(urls_table.c.id == id)
        await database.execute(query)
        return Response(status_code=204)

    except Exception as e:
        logging.error(e)
        return Response(status_code=500)


@router.get("/{short_url}")
async def short_to_big_url(short_url: str):

    query = urls_table.select().where(urls_table.c.short_url == short_url)
    record = await database.fetch_one(query)
    print(f"{record=}")
    if record is not None:
        redirect_url = record["url"]
        return RedirectResponse(redirect_url)
    else:
        return Response(status_code=404, content="Url not found")
