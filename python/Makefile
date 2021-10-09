
.DEFAULT_GOAL := test

PYTHON := python3

.PHONY: clean
clean:
	@echo 'Check the files/directories to delete:'
	@git clean -n -xdf | sed 's/^/    /'
	@echo 'Run following command:'
	@echo '    git clean -xdf'

.PHONY: run
run:
	PYTHONPATH=. ${PYTHON} main/main.py

.PHONY: test
test:
	PYTHONPATH=. ${PYTHON} -m 'unittest' discover -v -s test

.PHONY: stats
stats:
	@echo "# TODO"
	@find * -type f -name '*.py' | xargs grep -nP '# [A-Z]+ ' | sed 's/^/    /'
	@echo "# wc"
	@find koikoi test -type f -name '*.py' | xargs wc | sed 's/^/    /'

