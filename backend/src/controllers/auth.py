# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


from fastapi import APIRouter, Response, status
from fastapi import Depends, Security
from src.utils.auth import Auth0User, auth

router = APIRouter()


@router.get("/auth/public", dependencies=[Depends(auth.implicit_scheme)])
def public(user: Auth0User = Security(auth.get_user, scopes=[])):
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": (
            "Hello from a public endpoint! You don't need to be "
            "authenticated to see this."
        ),
    }
    return result


@router.get("/auth/secure", dependencies=[Depends(auth.implicit_scheme)])
def get_secure(user: Auth0User = Security(auth.get_user, scopes=[])):
    return {"message": f"{user}"}


# @router.get("/auth/private")
# def private(response: Response, token: str = Depends(token_auth_scheme)):
#     """A valid access token is required to access this route"""
#     result = VerifyToken(token.credentials).verify()
#     logging.debug(f"{result=}")
#     if result.get("status"):
#         response.status_code = status.HTTP_400_BAD_REQUEST
#         return result
#     return result
