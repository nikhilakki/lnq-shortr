# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter, Depends, Security
from src.utils.auth import auth, Auth0User
from src.services import url, GenerateShortURL

router = APIRouter()


@router.post(
    "/short-url", status_code=201)#, dependencies=[Depends(auth.implicit_scheme)])
async def shorten_url(
    generateShortURL: GenerateShortURL,
    # user: Auth0User = Security(auth.get_user, scopes=["user"]),
):
    return await url.shorten_url(generateShortURL)


@router.get(
    "/short-url/all", status_code=200)#, dependencies=[Depends(auth.implicit_scheme)])
async def get_url_all():#(user: Auth0User = Security(auth.get_user, scopes=["user"])):
    return await url.get_url_all()


@router.delete("/short-url/{id}")#, dependencies=[Depends(auth.implicit_scheme)])
async def delete_url(
    id: int):#, user: Auth0User = Security(auth.get_user, scopes=["user"])):
    return await url.delete_url(id)


@router.get("/{short_url}")
async def short_to_big_url(short_url: str):
    return await url.short_to_big_url(short_url)
