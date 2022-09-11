# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from email.policy import default
from sqlalchemy import (
    Column,
    Integer,
    String,
    Table,
    func,
    DateTime,
    Boolean,
    ForeignKey,
)
from . import metadata

quota_table = Table(
    "quota",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", String, ForeignKey("user.id"), nullable=False),
    Column("quota_usage", Integer, nullable=False),
    Column("total_limit", Integer, nullable=False, default=1000),
    Column("isActive", Boolean, default=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)
