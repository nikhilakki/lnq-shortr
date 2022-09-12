# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter, Security, Depends
from src.services import quota, QuotaDto
from src.utils.auth import auth, Auth0User

router = APIRouter()


@router.get("/quota/all", status_code=202, dependencies=[Depends(auth.implicit_scheme)])
async def getUsers(user: Auth0User = Security(auth.get_user, scopes=["admin"])):
    return await quota.getUsers()


@router.get(
    "/quota/{id}", status_code=202, dependencies=[Depends(auth.implicit_scheme)]
)
async def getUser(id: int, user: Auth0User = Security(auth.get_user, scopes=["admin"])):
    return await quota.getUser(id)


@router.post("/quota", status_code=201, dependencies=[Depends(auth.implicit_scheme)])
async def createUser(
    quotaDto: QuotaDto, user: Auth0User = Security(auth.get_user, scopes=["admin"])
):
    return await quota.createUser(quotaDto)


@router.patch(
    "/quota/{id}", status_code=200, dependencies=[Depends(auth.implicit_scheme)]
)
async def updateUser(
    quotaDto: QuotaDto,
    id: int,
    user: Auth0User = Security(auth.get_user, scopes=["admin"]),
):
    return await quota.updateUser(quotaDto, id)


@router.delete("/quota/{id}", dependencies=[Depends(auth.implicit_scheme)])
async def deleteUser(
    id: int, user: Auth0User = Security(auth.get_user, scopes=["admin"])
):
    return await quota.deleteUser(id)
