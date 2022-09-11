# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter
from fastapi.responses import Response
from pydantic import BaseModel
from src.models import database, user_table
from src.utils.logger import logger as logging


router = APIRouter()


class UserDto(BaseModel):
    name: str
    email: str
    isActive: bool = True


@router.get("/user/all", status_code=202)
async def getUsers():
    query = user_table.select()
    response = await database.fetch_all(query)
    logging.debug(f"{response=}")
    return response


@router.get("/user/{id}", status_code=202)
async def getUser(id: int):
    query = user_table.select().where(user_table.c.id == id)
    response = await database.fetch_one(query)
    logging.debug(f"{response=}")
    return response


@router.post("/user", status_code=201)
async def createUser(userDto: UserDto):
    query = user_table.insert().values({**userDto.dict()})
    response = await database.execute(query)
    logging.debug(f"{response=}")
    return {"id": response}


@router.patch("/user/{id}", status_code=200)
async def updateUser(userDto: UserDto, id: int):
    try:
        query = (
            user_table.update().where(user_table.c.id == id).values({**userDto.dict()})
        )
        response = await database.execute(query)
        logging.debug(f"{response=}")
        return Response(content="Success", status_code=200)
    except Exception as e:
        logging.error(f"Error = {e}")
        return Response(content="Something went wrong!", status_code=500)


@router.delete("/user/{id}")
async def deleteUser(id: int):
    try:
        query = user_table.delete().where(user_table.c.id == id)
        await database.execute(query)
        return Response(status_code=204)
    except Exception as e:
        logging.error(e)
        return Response(status_code=500)
