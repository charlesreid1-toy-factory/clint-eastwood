"""
Movies that Clint Eastwood has produced
"""
import os
import sys
import json
import random
import logging
import argparse

from eastwood.clint import dispatch


logger = logging.getLogger(__name__)


producer = dispatch.target("producer", arguments={}, help=__doc__)


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


@producer.action(
    "non-executive",
    arguments={
        "--json": json_flag_options,
        "--sort-by-value": sort_by_val_flag_options,
    },
)
def producer_nonexecutive(argv, args):
    """
    Clint Eastwood was listed as a Non-Executive Producer on these films
    """
    nonexec = [
        ("Pale Rider", 1985),
        ("Sudden Impact", 1983),
        ("Heartbreak Ridge", 1986),
        ("Honkytonk Man",   1982),
        ("Firefox", 1982),
        ("Tightrope", 1984),
    ]
    print_kv(argv, args, nonexec)


@producer.action(
    "executive",
    arguments={
        "--json": json_flag_options,
        "--sort-by-value": sort_by_val_flag_options,
    },
)
def producer_executive(argv, args):
    """
    Clint Eastwood was listed as an Executive Producer on these films
    """
    executive = [
        ("77 Sunset Strip", 1995),
        ("Dirty Harry", 1971),
        ("Ratboy", 1986),
        ("Hang Em High", 1968),
    ]
    print_kv(argv, args, executive)
