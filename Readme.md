# clint-eastwood

This repository is a demonstration of how to implement an
object-oriented command line tool with tests in Python.


## Quick Start

```
python3 scripts/ops.py --help
```


## Tests

Tests can be run with pytest:

```
pytest -vs tests/
```


## What is in this repo?

There are two main directories:

* `scripts/` directory:
    * `scripts/ops.py`: script that an
      operator will actually run with Python (`python3 scripts/ops.py`)
      when performing actions.

* `eastwood/` directory:
    * `eastwood/clint/`: contains classes defining the ops.py command line 
      tool's flags, options, behavior, and logic.

* `tests/` directory:
    * `tests/test_clint.py`
    * `tests/test_clint_think.py`
    * `tests/test_clint_house.py`
    * `tests/test_clint_water.py`
    * `tests/test_clint_utils.py`


## What is the point of this example?

The point is twofold:

* Presents a good pattern for having operational tooling that utilizes
  object-oriented code that can be maintained, tracked, and updated
  as part of a core library. This makes operational tooling more reliable,
  more useful, and easier to write tests for.

* Demonstrates some techniques for writing good tests, including
  having useful test utilities. Includes some good patterns from
  tests in the DSS data store.


## What is not included in this example?

Thisexample can be taken a step further.

The pattern that we are providing in this repository can be thought of as
an additional operations layer that can be added alongside an existing
library. This is useful for any software library that also has associated
infrastructure, and operational tooling is required to manage or interact
with existing resources, create new resources, or remove resources.


