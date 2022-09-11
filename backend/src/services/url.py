# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi.responses import RedirectResponse, Response
from pydantic import BaseModel
import validators
from src.core.hash import generate_url_hash
from src.models import database, urls_table
from src.utils.logger import logger as logging


class GenerateShortURL(BaseModel):
    name: str = None
    url: str
    user_id: str


async def shortended_url(generateShortURL: GenerateShortURL):
    try:
        url = generateShortURL.url
        name = generateShortURL.name

        validation = validators.url(url)
        if validation:
            short_url = generate_url_hash()
            query = urls_table.insert().values(name=name, url=url, short_url=short_url)
            record_id = await database.execute(query)
            response = {
                "response": dict(url=url, short_url=short_url, record_id=record_id)
            }
            return response
        else:
            return Response(status_code=400, content="Url not valid")
    except Exception as e:
        logging.error(f"{e}")
        return Response(content="Spmeting went wrong!", status_code=500)


async def all_records():
    query = urls_table.select()
    response = await database.fetch_all(query)
    return response


async def delete_record(id: int):
    try:
        query = urls_table.delete().where(urls_table.c.id == id)
        await database.execute(query)
        return Response(status_code=204)

    except Exception as e:
        logging.error(e)
        return Response(status_code=500)


async def short_to_big_url(short_url: str):
    query = urls_table.select().where(urls_table.c.short_url == short_url)
    record = await database.fetch_one(query)
    print(f"{record=}")
    if record is not None:
        redirect_url = record["url"]
        return RedirectResponse(redirect_url)
    else:
        return Response(status_code=404, content="Url not found")
