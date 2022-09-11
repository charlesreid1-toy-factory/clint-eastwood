"""
Characters that Clint Eastwood has played
"""
import os
import sys
import json
import random
import logging
import argparse

from eastwood.clint import dispatch


logger = logging.getLogger(__name__)


characters = dispatch.target("characters", arguments={}, help=__doc__)


# Set up dicts with common flag options for all the actions below
json_flag_options = dict(
    default=False, dest='_json', action="store_true", help="format the output as JSON if this flag is present"
)
sort_by_val_flag_options = dict(
    default=False, dest='_sort', action="store_true", help="sort the items being printed, by value (not key)"
)


def print_kv(argv, args, kvlist):
    if args._sort:
        # sort by value
        kvlist.sort(key = lambda x: x[1])

    if args._json:
        d = {k: v for (k, v) in kvlist}
        print(json.dumps(d, indent=4))

    else:
        print()
        for k, v in kvlist:
            print(f" - {k}: {v}")
        print()


@characters.action(
    "westerns",
    arguments={
        "--json": json_flag_options,
        "--sort-by-value": sort_by_val_flag_options,
    },
)
def characters_westerns(argv, args):
    """
    Characters in Western movies played by Clint Eastwood
    """
    westernchars = [
        ("The Outlaw Josey Wales", "Josey Wales"),
        ("High Plains Drifter", "The Stranger"),
        ("Unforgiven", "Bill Munny"),
        ("The Good the Bad, and the Ugly", "Blondie"),
        ("A Fistful of Dollars", "Joe"),
        ("For a Few Dollars More", "Monco"),
    ]
    print_kv(argv, args, westernchars)


@characters.action(
    "calahan",
    arguments={
        "--json": json_flag_options,
        "--sort-by-value": sort_by_val_flag_options,
    },
)
def characters_calahan(argv, args):
    """
    Movies starring Clint Eastwood as Inspector Harry Calahan
    """
    calahan = [
        ("Sudden Impact", 1983),
        ("The Dead Pool", 1988),
        ("Dirty Harry", 1971),
        ("The Enforcer", 1976),
        ("Magnum Force", 1973),
    ]
    print_kv(argv, args, calahan)
