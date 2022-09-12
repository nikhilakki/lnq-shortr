# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter, Depends, Security
from src.services import user, UserDto
from src.utils.auth import auth, Auth0User

router = APIRouter()


@router.get("/user/all", status_code=202, dependencies=[Depends(auth.implicit_scheme)])
async def getUsers(user: Auth0User = Security(auth.get_user, scopes=["admin"])):
    return await user.getUsers()


@router.get("/user/{id}", status_code=202, dependencies=[Depends(auth.implicit_scheme)])
async def getUser(id: int, user: Auth0User = Security(auth.get_user, scopes=["admin"])):
    return await user.getUser(id)


@router.post("/user", status_code=201, dependencies=[Depends(auth.implicit_scheme)])
async def createUser(
    userDto: UserDto, user: Auth0User = Security(auth.get_user, scopes=["admin"])
):
    return await user.createUser(userDto)


@router.patch(
    "/user/{id}", status_code=200, dependencies=[Depends(auth.implicit_scheme)]
)
async def updateUser(
    userDto: UserDto,
    id: int,
    user: Auth0User = Security(auth.get_user, scopes=["admin"]),
):
    return await user.updateUser(userDto, id)


@router.delete("/user/{id}", dependencies=[Depends(auth.implicit_scheme)])
async def deleteUser(
    id: int, user: Auth0User = Security(auth.get_user, scopes=["admin"])
):
    return await user.deleteUser(id)
