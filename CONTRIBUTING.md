# Contributing

This project uses [Poetry](https://python-poetry.org/) to manage dependencies, environments and execution.
It also uses [Docker](https://www.docker.com/) for running integration tests

Install all dependencies:
```bash
poetry install
```
Everything should be covered by tests, this project has been put together following TDD using `pytest`

Check all the tests are executing properly:
```bash
# Run only the Unit tests
poetry run pytest -m "not integration"

# Run only the Integration tests
poetry run pytest -m integration

# Run all tests (recommended)
poetry run pytest
```

Once changes have been made, use `black` and `isort` to format all the files:
```bash
# Format with black
poetry run black src/ tests/

# Format with isort
poetry run isort --profile=black src/ tests/
```