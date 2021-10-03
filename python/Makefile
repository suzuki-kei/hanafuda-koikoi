
.DEFAULT_GOAL := \test

\test:
	PYTHONPATH=. python3 -m 'unittest' discover -v -s test

stats:
	@echo "# TODO"
	@find * -type f -name '*.py' | xargs grep -P '# [A-Z]+ ' | sed 's/^/    /'
	@echo "# wc"
	@find koikoi test -type f -name '*.py' | xargs wc | sed 's/^/    /'

