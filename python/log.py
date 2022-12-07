from os import environ

from nc_py_api import cpa_logger

logger = cpa_logger.getChild("your_project_name")   # replace `your_project_name` with your app name.
logger.setLevel(level=environ.get("LOGLEVEL", "INFO").upper())
