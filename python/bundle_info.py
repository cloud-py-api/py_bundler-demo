import sys

import numpy
import pg8000
import PIL
import pymysql
import nc_py_api

from ._version import __version__
from .log import logger as log


def bundle_info():
    log.info("Python: %s", sys.version)
    log.info("your_project_name: %s", __version__)
    log.info("nc_py_api: %s", nc_py_api.__version__)
    log.info("pg8000: %s", pg8000.__version__)
    log.info("pymysql: %s", pymysql.__version__)
    log.info("pillow: %s", PIL.__version__)
    log.info("numpy: %s", numpy.__version__)
