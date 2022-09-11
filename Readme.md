# clint-eastwood

<img alt="version-0.1.0" src="https://img.shields.io/badge/version-0.1.0-orange" />

<img 
alt="tests-unittest" src="https://img.shields.io/badge/tests-unittest-green" /><img 
alt="tests-coverage" src="https://img.shields.io/badge/tests-coverage-green" />

<img alt="codestyle-flake8" src="https://img.shields.io/badge/codestyle-flake8-blue" />

<img alt="python-3.10" src="https://img.shields.io/badge/python-3.10-blue" />

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

To get help, just run the script with no arguments:

```
./scripts/ops.py
```

This will show you the short help menu:

```
$ ./scripts/ops.py
usage: ops.py [-h] {movies,dirty-harry-facts,characters,producer} ...

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
  {movies,dirty-harry-facts,characters,producer}
    movies
                        Movies starting Clint Eastwood
    dirty-harry-facts
                        Facts about Dirty Harry (via clinteastwood.net)
    characters
                        Characters that Clint Eastwood has played
    producer
                        Movies that Clint Eastwood has produced

optional arguments:
  -h, --help            Show this help message and exit
```

For a longer help menu, run the script with the `--help` flag.


## Running Tests

Use `make test` to run tests. This runs the tests via the coverage.py tool:

```
$ make test
/Library/Developer/CommandLineTools/usr/bin/make -j1 tests/test_operations_dispatch.py tests/test_operations_facts.py tests/test_operations_movies.py
flake8 tests
coverage run -p --source=eastwood tests/test_operations_dispatch.py
.
----------------------------------------------------------------------
Ran 1 test in 0.005s

OK
coverage run -p --source=eastwood tests/test_operations_facts.py
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
coverage run -p --source=eastwood tests/test_operations_movies.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Use `make coverage` to print a code coverage reoport:

```
$ make coverage
coverage combine
Combined data file .coverage.aptos.43424.252373
Combined data file .coverage.aptos.43425.753329
Combined data file .coverage.aptos.39915.988536
Combined data file .coverage.aptos.39914.274878
Combined data file .coverage.aptos.43423.645311
Combined data file .coverage.aptos.39916.541310
Combined data file .coverage.aptos.44633.985633
Combined data file .coverage.aptos.44634.956163
Combined data file .coverage.aptos.44635.326438
coverage report
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
eastwood/clint/__init__.py               55      6    89%
eastwood/clint/characters.py             29     29     0%
eastwood/clint/dirty_harry_facts.py      44      0   100%
eastwood/clint/movies.py                 41      0   100%
eastwood/clint/producer.py               29     29     0%
eastwood/clint/util.py                   27     27     0%
---------------------------------------------------------
TOTAL                                   225     91    60%
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

Some environment variables may need to be used by the operations script.

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

source environment
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

## Full Help Reference

Running with the `--help` flag will print help for all subcommands at once:

```
$ ./scripts/ops.py --help

usage: ops.py [--help] {movies,dirty-harry-facts,characters,producer} ...

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
  {movies,dirty-harry-facts,characters,producer}
    movies              
                        Movies starting Clint Eastwood
    dirty-harry-facts   
                        Facts about Dirty Harry (via clinteastwood.net)
    characters          
                        Characters that Clint Eastwood has played
    producer            
                        Movies that Clint Eastwood has produced

optional arguments:
  --help                Show this help message and exit

========================================
Eastwood Operation: 'movies'

usage: ops.py movies [-h] {westerns,crime,biography} ...

positional arguments:
  {westerns,crime,biography}
    westerns            Western movies starring Clint Eastwood
    crime               Crime movies starring Clint Eastwood
    biography           Biography movies starring Clint Eastwood

optional arguments:
  -h, --help            show this help message and exit


========================================
Eastwood Operation: 'dirty-harry-facts'

usage: ops.py dirty-harry-facts [-h] {partner,zoom,fivemin,water} ...

positional arguments:
  {partner,zoom,fivemin,water}
    partner             Facts about Dirty Harry's partner
    zoom                Facts about zooming in during Dirty Harry films
    fivemin             Facts about the first five minutes of Dirty Harry
                        films
    water               Facts about bodies of water in the Dirty Harry films

optional arguments:
  -h, --help            show this help message and exit


========================================
Eastwood Operation: 'characters'

usage: ops.py characters [-h] {westerns,calahan} ...

positional arguments:
  {westerns,calahan}
    westerns          Characters in Western movies played by Clint Eastwood
    calahan           Movies starring Clint Eastwood as Inspector Harry
                      Calahan

optional arguments:
  -h, --help          show this help message and exit


========================================
Eastwood Operation: 'producer'

usage: ops.py producer [-h] {non-executive,executive} ...

positional arguments:
  {non-executive,executive}
    non-executive       Clint Eastwood was listed as a Non-Executive Producer
                        on these films
    executive           Clint Eastwood was listed as an Executive Producer on
                        these films

optional arguments:
  -h, --help            show this help message and exit
```

