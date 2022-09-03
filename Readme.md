# clint-eastwood

This repository is a demonstration of how to implement an
object-oriented command line tool with tests in Python.


## Quick Start

```
python3 scripts/ops.py --help
```


## What is in this repo?

There are two main directories:

* `scripts/` contains one script, `ops.py`, which is the script that an
  operator will actually run with Python (`python3 scripts/ops.py`)
  when performing actions.

* `eastwood/` contains one subdirectory, `clint/`, that defines the
  command line tool's flags, options, and behavior.


## What is the point of this example?

The point is twofold:

* Presents a good pattern for having operational tooling that utilizes
  object-oriented code that can be maintained, tracked, and updated
  as part of a core library. This makes operational tooling more reliable,
  more useful, and easier to write tests for.

* Demonstrates some techniques for writing good tests, including
  having useful test utilities. Includes some good patterns from
  tests in the DSS data store.


