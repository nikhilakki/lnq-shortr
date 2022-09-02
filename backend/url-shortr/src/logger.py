# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import logging

logging.basicConfig(
    format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S", level=logging.DEBUG
)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug("Logger successfully loaded!")
