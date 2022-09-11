# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from enum import unique
from sqlalchemy import Column, Integer, String, Table, func, DateTime, Boolean
from . import metadata


user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String, unique=True),
    Column("isActive", Boolean, default=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)
