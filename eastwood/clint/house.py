"""
Get back in the house
"""
import os
import sys
import json
import random
import logging
import argparse

from eastwood.clint import dispatch


logger = logging.getLogger(__name__)


def get_location() -> str:
    value = os.environ.get("CLINT_EASTWOOD_LOCATION", '127.0.0.1')
    return value


water = dispatch.target("house", arguments={}, help=__doc__)


# Set up dicts with common flag options for all the actions below
quiet_flag_options = dict(
    default=False, action="store_true", help="suppress output"
)


@water.action(
    "achoo",
    arguments={
        "--quiet": quiet_flag_options,
    },
)
def house_pssst(argv, args):
    """
    pssst, get back in the house
    """
    msg = "pssst, get back in the house"
    if args.quiet:
        print(msg.lower())
    if args.quiet:
        print(msg.upper())
