"""
Water something
"""
import os
import sys
import json
import random
import logging
import argparse

from eastwood.clint import dispatch


logger = logging.getLogger(__name__)


def get_beverage() -> str:
    value = os.environ.get("CLINT_EASTWOOD_BEVERAGE", 'water')
    return value


water = dispatch.target("water", arguments={}, help=__doc__)


# Set up dicts with common flag options for all the actions below
json_flag_options = dict(
    default=False, action="store_true", help="format the output as JSON if this flag is present"
)


@water.action(
    "achoo",
    arguments={
        "--json": json_flag_options,
    },
)
def water_achoo(argv, args):
    """
    Water the achoo. Say achoo forty times.
    """
    sneeze = ["achoo! ",]*40
    if args.json:
        print(json.dumps(sneeze, indent=4))
    else:
        print("".join(sneeze))

