# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter
from src.services import quota, QuotaDto


router = APIRouter()


@router.get("/quota/all", status_code=202)
async def getUsers():
    return await quota.getUsers()


@router.get("/quota/{id}", status_code=202)
async def getUser(id: int):
    return await quota.getUser(id)


@router.post("/quota", status_code=201)
async def createUser(quotaDto: QuotaDto):
    return await quota.createUser(quotaDto)


@router.patch("/quota/{id}", status_code=200)
async def updateUser(quotaDto: QuotaDto, id: int):
    return await quota.updateUser(quotaDto, id)


@router.delete("/quota/{id}")
async def deleteUser(id: int):
    return await quota.deleteUser(id)
