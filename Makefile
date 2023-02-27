.PHONY: fmt
fmt:
	poetry run black src/ tests/
	poetry run isort --profile=black src/ tests/

.PHONY: fmtxml
fmtxml: fmt
	find tests/test_files -type f -name "*.xml" -exec poetry run xmlformat --indent 4 --overwrite {} \;

.PHONY: unittest
unittest: fmt
	poetry run pytest -m "not integration" -vv

.PHONY: integration
integration: fmt
	poetry run pytest -m integration -vv

.PHONY: test
test: fmt
	poetry run pytest -vv