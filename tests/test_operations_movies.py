import io
import os
import sys
import uuid
import json
import logging
import argparse
import unittest
import string
import random
import copy
import datetime
import tempfile
import typing

from collections import namedtuple
from unittest import mock

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # noqa
sys.path.insert(0, pkg_root)  # noqa

from tests.util import CaptureStdout  # SwapStdin

# from tests import skip_on_travis
# from tests.infra import testmode

from eastwood.clint import EastwoodOperationsCommandDispatch
from eastwood.clint import movies


class TestOperationsMovies(unittest.TestCase):
    def test_movies(self):
        # Each subcommand has identical flags
        subcommands = ["westerns", "crime", "biography"]

        known_movies = {
            "westerns": ["High Plains Drifter", "Unforgiven"],
            "crime": ["Mystic River", "Dirty Harry"],
            "biography": ["Bird", "Sully"],
        }

        for sub in subcommands:
            with self.subTest(f"testing operations script, movies command, {sub} subcommand"):

                argv = []

                # Get the function handle corresponding to this CLI call
                f = getattr(movies, f"movies_{sub}")

                # Plain formatting first
                args = argparse.Namespace(_json=False, _sort=False)
                with CaptureStdout() as output:
                    f(argv, args)
                for known_movie in known_movies[sub]:
                    self.assertIn(known_movie, output)

                # Check when json flag added we get json back
                args = argparse.Namespace(_json=True, _sort=False)
                with CaptureStdout() as output:
                    f(argv, args)
                result = json.loads("".join(output))
                self.assertGreater(len(result), 0)

                # Check that if we ask for sorted,
                #  then return and sorted is the same as returned
                args = argparse.Namespace(_json=False, _sort=True)
                with CaptureStdout() as output:
                    f(argv, args)

                # Ensure empty lines are discarded
                output = [o for o in output if len(o) > 0]
                output_sorted = sorted(output)
                self.assertListEqual(output, output_sorted)


#                with SwapStdin(testvar_value):
#                    secrets.set_secret(
#                        [],
#                        argparse.Namespace(
#                            secret_name=testvar_name, dry_run=True, infile=None, quiet=True, force=True
#                        ),
#                    )
#
# ################# meanwhile...
#
#                  @secrets.action(
#                      "set",
#                      arguments={
#                          "secret_name": dict(help="name of secret to set (limit 1 at a time)"),
#                          "--infile": dict(help="specify an input file whose contents is the secret value"),
#                          "--force": dict(
#                              default=False, action="store_true", help="force the action to happen (no interactive prompt)"
#                          ),
#                          "--dry-run": dryrun_flag_options,
#                          "--quiet": quiet_flag_options
#                      },
#                  )
#                  def set_secret(argv: typing.List[str], args: argparse.Namespace):


if __name__ == "__main__":
    unittest.main()
