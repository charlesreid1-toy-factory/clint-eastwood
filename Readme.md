# clint-eastwood

![Clint Eastwood](img/clint.jpg)

This repository is a demonstration of how to implement an
object-oriented command line tool, with tests, in Python.


## Quick Start

The main script is at `scripts/ops.py`. It can be run through Python,
or just run directly. Basic usage is:

```
./scripts/ops.py <action>
```

To get help:

```
./scripts/ops.py --help 
```

This will show you the help menu, with each possible action listed at the bottom.

```
$ ./scripts/ops.py --help


usage: ops.py [-h] {think,water,house} ...

    Grand central dispatch for Eastwood operations
   
                              .
                        .MMMMMP    Go ahead. Make my day.
                      .MM888MM
....                .MM88888MP
MMMMMMMMb.         d8MM8tt8MM
 MM88888MMMMc `:' dMME8ttt8MM
  MM88tt888EMMc:dMM8E88tt88MP
   MM8ttt888EEM8MMEEE8E888MC
   `MM888t8EEEM8MMEEE8t8888Mb
    "MM88888tEM8"MME88ttt88MM
     dM88ttt8EM8"MMM888ttt8MM
     MM8ttt88MM" " "MMNICKMM"
     3M88888MM"      "MMMP"
      "MNICKM"
   
    

positional arguments:
  {think,water,house}
    think              
                       Do a think
    water              
                       Water something
    house              
                       Get back in the house

options:
  -h, --help           show this help message and exit
```


## Environment Files

There are several environment variables used by the operations script.

The provided `environment.example` file shows an example of how to set
those environment variable values.

Copy `environment.example` to `environment`, and edit the environment
variable values. When finished, run `source environment` before running
the operations script.


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


