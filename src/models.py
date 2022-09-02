import os
import logging
import databases
import sqlalchemy

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

if os.getenv("PROD", False):
    # SQLAlchemy specific code, as with any other app
    DATABASE_URL = os.getenv(
        "PGSQL_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
    )
else:
    DATABASE_URL = os.getenv("SQLITE3_URI", "sqlite:///./app.db")

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

if __name__ == "__main__":
    metadata.create_all(engine)
    logging.info("Table created!")
