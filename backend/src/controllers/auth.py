# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


from fastapi import APIRouter, Response, status
from fastapi import Security
from src import azure_scheme

router = APIRouter()


@router.get("/auth/public", dependencies=[Security(azure_scheme)])
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": (
            "Hello from a public endpoint! You don't need to be "
            "authenticated to see this."
        ),
    }
    return result


@router.get("/auth/secure", dependencies=[Security(azure_scheme)])
def get_secure():
    return {"message": f"{user}"}
