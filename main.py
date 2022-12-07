import argparse
import sys

from nc_py_api import CONFIG

from python.bundle_info import bundle_info
from python.log import logger as log


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Skeletal sample application in Python", add_help=True)
    group = parser.add_mutually_exclusive_group()
    # here register all commands if any
    group.add_argument(
        "-ls",
        dest="list_files",
        type=str,
        action="append",
        help="List files",
    )
    # next command is required and is used by framework
    group.add_argument(
        "--info", dest="bundle_info", action="store_true", help="Print information about bundled packages."
    )
    args = parser.parse_args()
    if args.bundle_info:
        # inside this command it is recommended to import and print all top level libraries used by your app
        bundle_info()
    elif args.list_files:
        # these lines are needed for situations when for some reason we cannot connect to the database.
        if not CONFIG["valid"]:
            log.error("Unable to parse config or connect to database. Does `occ` works?")
            sys.exit(1)
        # here goes your code ->
        log.error("will implement soon here FS example :)")
    else:
        parser.print_help()
    sys.exit(0)
