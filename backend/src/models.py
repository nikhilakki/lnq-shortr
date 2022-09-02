from enum import unique
import os
from uuid import UUID
import databases
import sqlalchemy
import logging

DATABASE_URL = os.getenv(
    "PGSQL_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

urls_table = sqlalchemy.Table(
    "urls",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("url", sqlalchemy.String),
    sqlalchemy.Column("short_url", sqlalchemy.String, unique=True),
)


engine = sqlalchemy.create_engine(DATABASE_URL)

if __name__ == "__main__":
    metadata.create_all(engine)
    logging.info("Table created!")
