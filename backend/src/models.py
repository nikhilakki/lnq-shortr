from email.policy import default
from enum import unique
import os
import logging
import databases
import sqlalchemy
from sqlalchemy.sql import func


DATABASE_URL = os.getenv(
    "PGSQL_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

urls_table = sqlalchemy.Table(
    "urls",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("url", sqlalchemy.String),
    sqlalchemy.Column("short_url", sqlalchemy.String, unique=True),
    sqlalchemy.Column("isActive", sqlalchemy.Boolean, default=True),
    sqlalchemy.Column(
        "created_at", sqlalchemy.DateTime(timezone=True), server_default=func.now()
    ),
    sqlalchemy.Column(
        "updated_at", sqlalchemy.DateTime(timezone=True), onupdate=func.now()
    ),
)


engine = sqlalchemy.create_engine(DATABASE_URL)

if __name__ == "__main__":
    metadata.create_all(engine)
    logging.info("Table created!")
