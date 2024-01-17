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
make unittest

# Run only the Integration tests
make integration

# Run all tests (recommended)
make test
```

To ensure all code is covered by tests, a coverage report can be generated. This command will fail if coverage is not 100% and highlight where tests are missing
```bash
# When developing with unit tests only
make unittest coverage

# When creating integration tests
make test coverage
```

Once changes have been made, use `black` and `isort` to format all the files:
```bash
# Format with black
make fmt

# If adding XML files, they can also be formatted
make fmtxml
```