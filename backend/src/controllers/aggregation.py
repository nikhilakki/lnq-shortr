# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""
Aggregation layer
"""

from fastapi import APIRouter


router = APIRouter()


@router.post("/short-url")
def generateShortUrl():
    