.PHONY: fmt
fmt:
	poetry run black src/ tests/
	poetry run isort --profile=black src/ tests/

.PHONY: fmtxml
fmtxml: fmt
	find tests/test_files -type f -name "*.xml" -exec echo "- {}" \; -exec poetry run xmlformat --indent 4 --overwrite {} \;

.PHONY: unittest
unittest: fmt
	poetry run coverage run --data-file cov/unittest.coverage -m pytest -m "not integration and not authenticated" -vv

.PHONY: integration
integration: fmt
	poetry run coverage run --data-file cov/integration.coverage -m pytest -m "integration" -vv

.PHONY: authenticated
authenticated: fmt
	poetry run coverage run --data-file cov/authenticated.coverage -m pytest -m "authenticated" -vv

.PHONY: test
test: unittest integration authenticated

.PHONY: coverage
coverage:
	poetry run coverage combine --keep --data-file cov/.coverage cov/*.coverage
	poetry run coverage report --show-missing --data-file cov/.coverage --omit "tests/*,src/boinc_client/clients/rpc_client.py" --fail-under=100