
\test:
	PYTHONPATH=. python3 -m 'unittest' discover -v -s test

stats:
	@echo "# TODO"
	@find koikoi test -type f -name '*.py' | xargs grep -F TODO | sed 's/^/    /'
	@echo "# wc"
	@find koikoi test -type f -name '*.py' | xargs wc | sed 's/^/    /'

