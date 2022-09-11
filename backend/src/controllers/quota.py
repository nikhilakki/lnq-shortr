# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter
from fastapi.responses import Response
from pydantic import BaseModel
from src.models import database, quota_table
from src.utils.logger import logger as logging


router = APIRouter()


class QuotaDto(BaseModel):
    user_id: int
    quota_usage: int
    total_limit: int = 1000
    isActive: bool = True


@router.get("/quota/all", status_code=202)
async def getUsers():
    query = quota_table.select()
    response = await database.fetch_all(query)
    logging.debug(f"{response=}")
    return response


@router.get("/quota/{id}", status_code=202)
async def getUser(id: int):
    query = quota_table.select().where(quota_table.c.id == id)
    response = await database.fetch_one(query)
    logging.debug(f"{response=}")
    return response


@router.post("/quota", status_code=201)
async def createUser(quotaDto: QuotaDto):
    query = quota_table.insert().values({**quotaDto.dict()})
    response = await database.execute(query)
    logging.debug(f"{response=}")
    return {"id": response}


@router.patch("/quota/{id}", status_code=200)
async def updateUser(quotaDto: QuotaDto, id: int):
    try:
        query = (
            quota_table.update()
            .where(quota_table.c.id == id)
            .values({**quotaDto.dict()})
        )
        response = await database.execute(query)
        logging.debug(f"{response=}")
        return Response(content="Success", status_code=200)
    except Exception as e:
        logging.error(f"Error = {e}")
        return Response(content="Something went wrong!", status_code=500)


@router.delete("/quota/{id}")
async def deleteUser(id: int):
    try:
        query = quota_table.delete().where(quota_table.c.id == id)
        await database.execute(query)
        return Response(status_code=204)
    except Exception as e:
        logging.error(e)
        return Response(status_code=500)
