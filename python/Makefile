
.DEFAULT_GOAL := \test

PYTHON := python3

\test:
	PYTHONPATH=. ${PYTHON} -m 'unittest' discover -v -s test

stats:
	@echo "# TODO"
	@find * -type f -name '*.py' | xargs grep -nP '# [A-Z]+ ' | sed 's/^/    /'
	@echo "# wc"
	@find koikoi test -type f -name '*.py' | xargs wc | sed 's/^/    /'

