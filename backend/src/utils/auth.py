# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi_auth0 import Auth0, Auth0User
from src import settings


auth = Auth0(domain=settings.DOMAIN, api_audience=settings.API_AUDIENCE)
