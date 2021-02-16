"""Entry-point module for doxacal command-line interface."""

import argparse
import datetime
import logging
import sys

logging.basicConfig(format="%(message)s", level=logging.INFO)
package_logger = logging.getLogger(__package__)


def parse_date(date_string):
    """Parse a date given on the command-line."""
    try:
        return datetime.datetime.strptime(date_string, "%Y%m%d")
    except ValueError as value_error:
        msg = "Date format should be 'YYYYMMDD', e.g. '20210101'."
        raise argparse.ArgumentTypeError(msg) from value_error


def main(args=None):
    """Entry-point function for doxacal command-line interface."""
    parser = argparse.ArgumentParser(description="Orthodox Christian Calendar utility.")
    parser.add_argument(
        "-d",
        "--date",
        type=parse_date,
        default=datetime.date.today(),
        help="calendar date to search for, omit for today or use 'YYYYMMDD' formatting,"
        "e.g. '20210101'",
    )
    args = parser.parse_args(args)
    package_logger.info("Happy %s!", args.date.strftime("%Y-%m-%d"))


if __name__ == "__main__":
    sys.exit(main())
