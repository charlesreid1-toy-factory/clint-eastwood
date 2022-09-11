#!/usr/bin/env python
"""
Central entrypoint for clint-eastwood
"""
import os
import sys
import logging

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # noqa
sys.path.insert(0, pkg_root)  # noqa

import eastwood
import eastwood.clint.movies
import eastwood.clint.dirty_harry_facts
import eastwood.clint.characters
#import eastwood.clint.producer
#import eastwood.clint.quotes
#import eastwood.clint.facts

from eastwood.clint import dispatch

logging.basicConfig(stream=sys.stdout)


if __name__ == "__main__":
    dispatch(sys.argv[1:])
