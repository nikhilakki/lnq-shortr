# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter, Security
from src.services import quota, QuotaDto
from src import azure_scheme


router = APIRouter()


@router.get("/quota/all", status_code=202, dependencies=[Security(azure_scheme)])
async def getUser():
    return await quota.getUsers()


@router.get("/quota/{id}", status_code=202, dependencies=[Security(azure_scheme)])
async def getUser(id: int):
    return await quota.getUser(id)


@router.post("/quota", status_code=201, dependencies=[Security(azure_scheme)])
async def createUser(quotaDto: QuotaDto):
    return await quota.createUser(quotaDto)


@router.patch("/quota/{id}", status_code=200, dependencies=[Security(azure_scheme)])
async def updateUser(quotaDto: QuotaDto, id: int):
    return await quota.updateUser(quotaDto, id)


@router.delete("/quota/{id}", dependencies=[Security(azure_scheme)])
async def deleteUser(id: int):
    return await quota.deleteUser(id)
