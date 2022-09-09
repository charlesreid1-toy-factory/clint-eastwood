# clint-eastwood

![Clint Eastwood](img/clint.jpg)

This repository is a demonstration of how to implement an
object-oriented command line tool with Python,
and add tests with unittest and coverage.


## Quick Start

Before you begin, you will need to set up environment variables:

```
cp environment.example environment
```

Edit environment to set the variable values.

The main operations script is at `scripts/ops.py`.
It can be run through Python, or just run directly.
Basic usage is:

```
./scripts/ops.py <action>
```

To get help:

```
./scripts/ops.py --help 
```

This will show you the help menu:

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


## Running Tests

Use `make test` to run tests. This runs the tests via
the coverage tool, and prints a code coverage report.

```
$ make test

/Library/Developer/CommandLineTools/usr/bin/make -j1 tests/test_operations.py
flake8 tests
coverage run -p --source=eastwood tests/test_operations.py
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK
coverage combine
Combined data file .coverage.aptos.14785.069198
coverage report
Name                         Stmts   Miss  Cover
------------------------------------------------
eastwood/clint/__init__.py      55      6    89%
eastwood/clint/house.py         19      6    68%
eastwood/clint/think.py         77     53    31%
eastwood/clint/util.py          27     17    37%
eastwood/clint/water.py         19      6    68%
------------------------------------------------
TOTAL                          197     88    55%
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
    * `tests/test_operations.py`


### Environment File

There are several environment variables used by the operations script.

The pattern we provide for managing environment variables, which can
sometimes contain sensitive information, is to define them in a file
`environment`, and have the user run this command from the repo
before running any other actions:

```
source environment
```

The `environment` file is not under version control, to prevent sensitive
information from ending up in a git repository. Instead, we provide
an `environment.example` file:

```
cp environment.example environment

# Edit environment
```


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

This pattern - the operations script - is like a layer that can
go on top of an existing library. The `eastwood` directory does not
contain a full library, but it easily could. Likewise, some tests
would test core `eastwood` library functionality, while other
tests would only test the operational command line tool.

This is useful for a software library that is being deployed
along with infrastructure.
