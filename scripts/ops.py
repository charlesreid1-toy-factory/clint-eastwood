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
import eastwood.clint.think
import eastwood.clint.water
import eastwood.clint.house

# import eastwood.clint.small
# import eastwood.clint.large
# import eastwood.clint.story
# import eastwood.clint.power
# import eastwood.clint.above
# import eastwood.clint.below

from eastwood.clint import dispatch

logging.basicConfig(stream=sys.stdout)


if __name__ == "__main__":
    dispatch(sys.argv[1:])
