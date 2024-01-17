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

Once changes have been made, use `black` and `isort` to format all the files:
```bash
# Format with black
make fmt

# If adding XML files, they can also be formatted
make fmtxml
```