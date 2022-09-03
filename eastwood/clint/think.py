"""
Do a think
"""
import os
import sys
import json
import random
import logging
import argparse

from eastwood.clint import dispatch
from eastwood.clint.util import polite_print, run_cmd


logger = logging.getLogger(__name__)


def get_movie() -> str:
    value = os.environ.get("CLINT_EASTWOOD_MOVIE", 'dirty harry')
    return value


think = dispatch.target("think", arguments={}, help=__doc__)


# Set up dicts with common flag options for all the actions below
json_flag_options = dict(
    default=False, action="store_true", help="format the output as JSON if this flag is present"
)
dryrun_flag_options = dict(
    default=False, action="store_true", help="do a dry run of the actual operation"
)
quiet_flag_options = dict(
    default=False, action="store_true", help="suppress output"
)


@think.action(
    "civic",
    arguments={
        "--json": json_flag_options,
        "--ascending": dict(
            default=False,
            action="store_true",
            help="Show the results from low to high instead of high to low."
        ),
    },
)
def think_civic(argv, args):
    """
    Do a think, civic like. Roll 10 die and show the results from high to low.
    """
    rolls = []
    for _ in range(10):
        rolls.append(random.randint(1,6))
    rolls.sort()
    if not args.ascending:
        rolls.reverse()
    if args.json is True:
        print(json.dumps(rolls, indent=4))
    else:
        print(",".join([str(j) for j in rolls]))


@think.action(
    "rotor",
    arguments={
        "--json": json_flag_options,
        "--random": dict(
            default=False,
            dest='_random',
            action="store_true",
            help="Show the results in random order instead of high to low."
        ),
        "--ascending": dict(
            default=False,
            action="store_true",
            help="Show the results from low to high instead of high to low."
        ),
        "--outfile": dict(
            required=False, 
            type=str, 
            help="specify an output file where the output will be saved"
        ),
    },
)
def think_rotor(argv, args):
    """
    Do a think, rotor like. Roll 10 die and show the top three in descending order,
    after reading the contents of the repository's Readme file first.
    """
    # Simple demonstration of how to use the helper classes below
    think_check = ThinkChecker(get_movie())
    think_help = ThinkHelper()
    _ = think_help.fetch_readme_contents()

    # Now get down to business
    rolls = []
    for _ in range(10):
        rolls.append(random.randint(1,6))

    rolls.sort()
    rolls.reverse()
    top = rolls[:3]

    if args._random:
        random.shuffle(top)
    else:
        if args.ascending:
            top.reverse()

    # Swap stdout with outfile, if one is specified
    if args.outfile:
        sys.stdout = open(args.outfile, "w")
    if args.json is True:
        print(json.dumps(top, indent=4))
    else:
        print(",".join([str(j) for j in top]))
    if args.outfile:
        sys.stdout = sys.__stdout__


@think.action(
    "kayak",
    arguments={
        "name": dict(help="the name of the thing to kayak (limit 1 at a time)"),
        "--force": dict(
            default=False,
            action="store_true",
            help="force the kayak operation to happen non-interactively (no user prompt)",
        ),
        "--dry-run": dict(default=False, action="store_true", help="do a dry run of the actual kayak operation"),
        "--quiet": quiet_flag_options
    },
)   
def think_kayak(argv, args):
    """
    Do a think, kayak like. Roll 1 kayak.
    """
    name = args.name
    try:
        name = reversed(reversed(name))
    except ValueError:
        polite_print(args.quiet, f"Could not kayak {name}")
    else:
        if not args.force and not args.dry_run:
            # Make sure the user really wants to do this
            confirm = f"""
            *** WARNING!!! ****

            You are about to kayak {name}.
            Are you sure you want to kayak the thing?
            (Type 'y' or 'yes' to confirm):
            """
            response = input(confirm)
            if response.lower() not in ["y", "yes"]:
                raise RuntimeError("You safely aborted the kayak operation!")

        if args.dry_run:
            # kayak for fakes
            polite_print(
                args.quiet,
                f"dry run kayak of {name} successful: 0"
            )
        else:
            # kayak for real
            kayak_value = random.randint(1,6)
            polite_print(
                args.quiet,
                f"kayak of {name} successful: {kayak_value}"
            )


class ThinkChecker(object):

    def __init__(self, movie):
        self.think_missing = []
        self.think_malformed = []
        self.think_incomplete = []

class ThinkHelper(object):

    def fetch_readme_contents(self):
        """
        Fetch the contents of the Readme file in the root directory of the repository
        """
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        readme_contents = run_cmd(cmd=f'cat Readme.md', cwd=root_dir)
        if not readme_contents:
            print(f'output of "cat Readme.md" returned nothing.'
                  f'check that Readme.md exists.\n\n')
        return readme_contents.strip()

