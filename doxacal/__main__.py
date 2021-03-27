"""Entry-point module for doxacal command-line interface."""

import argparse
import datetime
import logging
import sys

from . import celebrations
from .version import __version__

logging.basicConfig(format="%(message)s", level=logging.INFO)
package_logger = logging.getLogger(__package__)


def parse_date(date_string):
    """Parse a date given on the command-line."""
    try:
        return datetime.datetime.strptime(date_string, "%Y%m%d")
    except ValueError as value_error:
        msg = "Date format should be 'YYYYMMDD', e.g. '20210101'."
        raise argparse.ArgumentTypeError(msg) from value_error


def get_args(args=None):
    """Process command-line arguments to be used in main function."""
    parser = argparse.ArgumentParser(description="Orthodox Christian Calendar utility.")
    parser.add_argument(
        "-d",
        "--date",
        type=parse_date,
        default=datetime.date.today(),
        help="calendar date to search for, omit for today or use 'YYYYMMDD' formatting, "
        "e.g. '20210101'",
    )
    parser.add_argument(
        "-p",
        "--pascha",
        dest="show_pascha",
        action="store_true",
        help="show the date of Pascha along with any other results",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="display version and exit",
    )
    return parser.parse_args(args)


def main(args=None):
    """Entry-point function for doxacal command-line interface."""
    args = get_args(args)
    package_logger.info("Happy %s!", args.date.strftime("%Y-%m-%d"))
    if args.show_pascha:
        year_string = args.date.strftime("%Y")
        try:
            pascha_date = celebrations.get_date_of_pascha(args.date)
            pascha_string = pascha_date.strftime("%b-%d")
            package_logger.info(
                "The date of Pascha for %s is %s.", year_string, pascha_string
            )
        except celebrations.DateNotFound:
            package_logger.error(
                "Could not find the date of Pascha for %s, sorry.", year_string
            )


if __name__ == "__main__":
    sys.exit(main())
