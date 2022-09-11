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
from eastwood.clint import dirty_harry_facts


class TestOperationsDirtyHarryFacts(unittest.TestCase):
    def test_facts_non_empty(self):
        # Smoke test to make sure things operate okay
        subcommands = ["partner", "zoom", "fivemin", "water"]

        for sub in subcommands:
            with self.subTest(
                f"testing operations script, dirty-harry-facts command, {sub} subcommand"
            ):

                argv = []

                # Get the function handle corresponding to this CLI call
                f = getattr(dirty_harry_facts, f"facts_{sub}")

                for _json_val in [True, False]:
                    for _shout_val in [True, False]:
                        args = argparse.Namespace(_json=_json_val, _shout=_shout_val)
                        with CaptureStdout() as _:
                            f(argv, args)


if __name__ == "__main__":
    unittest.main()
