SHELL=/bin/bash

ifeq ($(shell which flake8),)
$(error Please install flake8 or activate your virtual environment)
endif
