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
        print(json.dumps(westerns, indent=4))
    else:
        print()
        print("\n".join(westerns))
        print()


@movies.action(
    "crime",
    arguments={
        "--json": json_flag_options,
        "--sort": sort_flag_options,
    },
)
def movies_crime(argv, args):
    """
    Crime movies starring Clint Eastwood
    """
    crimes = [
        "Mystic River",
        "Dirty Harry",
        "Magnum Force",
        "The Mule",
        "Absolute Power",
        "In the Line of Fire",
        "Escape from Alcatraz",
    ]
    if args._sort:
        crimes.sort()
    if args._json:
        print(json.dumps(crimes, indent=4))
    else:
        print()
        print("\n".join(crimes))
        print()


@movies.action(
    "biography",
    arguments={
        "--json": json_flag_options,
        "--sort": sort_flag_options,
    },
)
def movies_biography(argv, args):
    """
    Biography movies starring Clint Eastwood
    """
    bios = [
        "American Sniper",
        "Sully",
        "Changeling",
        "Invictus",
        "Bird",
    ]
    if args._sort:
        bios.sort()
    if args._json:
        print(json.dumps(bios, indent=4))
    else:
        print()
        print("\n".join(bios))
        print()


