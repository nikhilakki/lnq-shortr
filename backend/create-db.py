# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from src.logger import logging
from src.models import metadata, engine

if __name__ == "__main__":
    metadata.create_all(engine)
    logging.info("Table created!")
