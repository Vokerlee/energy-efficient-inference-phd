PYTHON := ../.tools/python/bin/python

.PHONY: test lint

test:
	$(PYTHON) -m unittest discover -s . -p 'test_*.py'

lint:
	$(PYTHON) -m ruff check .
