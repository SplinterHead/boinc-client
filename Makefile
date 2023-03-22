.PHONY: fmt
fmt:
	poetry run black src/ tests/
	poetry run isort --profile=black src/ tests/

.PHONY: fmtxml
fmtxml: fmt
	find tests/test_files -type f -name "*.xml" -exec poetry run xmlformat --indent 4 --overwrite {} \;

.PHONY: unittest
unittest: fmt
	poetry run pytest -m "not integration and not authenticated" -vv -s

.PHONY: integration
integration: fmt
	poetry run pytest -m "integration and not authenticated" -vv -s

.PHONY: authenticated
authenticated: fmt
	poetry run pytest -m authenticated -vv -s

.PHONY: test
test: fmt
	poetry run pytest -vv