import sys

import nc_py_api

from ._version import __version__
from .log import logger as log


def bundle_info():
    log.info("Python: %s", sys.version)
    log.info("your_project_name: %s", __version__)
    log.info("nc_py_api: %s", nc_py_api.__version__)
