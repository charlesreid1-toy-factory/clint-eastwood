include common.mk
MODULES=tests

all: test

lint:
	flake8 $(MODULES)

# Vars
# 
tests:=$(wildcard tests/test_*.py)

# Run standalone tests 
# 
test:
	$(MAKE) -j1 $(tests)

# A pattern rule that runs a single test script
#
$(tests): %.py : lint
	coverage run -p --source=eastwood $*.py

.PHONY: all lint test safe_test serial_test all_test $(tests)
