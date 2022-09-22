# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter, Security
from src.services import user, UserDto
from src import azure_scheme

router = APIRouter()


@router.get("/user/all", status_code=202, dependencies=[Security(azure_scheme)])
async def getUsers():
    return await user.getUsers()


@router.get("/user/{id}", status_code=202, dependencies=[Security(azure_scheme)])
async def getUser(
    id: int,
):
    return await user.getUser(id)


@router.post("/user", status_code=201, dependencies=[Security(azure_scheme)])
async def createUser(
    userDto: UserDto,
):
    return await user.createUser(userDto)


@router.patch("/user/{id}", status_code=200, dependencies=[Security(azure_scheme)])
async def updateUser(
    userDto: UserDto,
    id: int,
):
    return await user.updateUser(userDto, id)


@router.delete("/user/{id}", dependencies=[Security(azure_scheme)])
async def deleteUser(
    id: int,
):
    return await user.deleteUser(id)
