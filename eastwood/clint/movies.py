"""
Movies starting Clint Eastwood
"""
import os
import sys
import json
import random
import logging
import argparse

from eastwood.clint import dispatch


logger = logging.getLogger(__name__)


movies = dispatch.target("movies", arguments={}, help=__doc__)


# Set up dicts with common flag options for all the actions below
json_flag_options = dict(
    default=False, dest='_json', action="store_true", help="format the output as JSON if this flag is present"
)
sort_flag_options = dict(
    default=False, dest='_sort', action="store_true", help="sort the names of movies being printed"
)


@movies.action(
    "westerns",
    arguments={
        "--json": json_flag_options,
        "--sort": sort_flag_options,
    },
)
def movies_westerns(argv, args):
    """
    Western movies starring Clint Eastwood
    """
    westerns = [
        "Unforgiven",
        "The Good the Bad, and the Ugly",
        "High Plains Drifter",
        "The Outlaw Josey Wales",
        "A Fistful of Dollars",
        "For a Few Dollars More",
    ]
    if args._sort:
        westerns.sort()
    if args._json:
        print(json.dumps(western, indent=4))
    else:
        print()
        print("\n".join(westerns))
        print()

