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
# (the -p flag means parallel, which also requires a combine step)
#
$(tests): %.py : lint
	coverage run -p --source=eastwood $*.py
	coverage combine
	coverage report

.PHONY: all lint test safe_test serial_test all_test $(tests)
