# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


import os
import databases
import sqlalchemy


DATABASE_URL = os.getenv(
    "DATABASE_URI",
    f"sqlite:///{os.path.join(os.getcwd(), 'app.db')}?check_same_thread=False",
)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

from .quota import quota_table
from .url import urls_table
from .user import user_table

engine = sqlalchemy.create_engine(DATABASE_URL)
