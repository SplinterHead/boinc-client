# Copilot instructions for boinc-client

## Build, test, and formatting commands

This repository uses Poetry for dependency and environment management.

```bash
poetry install

# Build distributable package
poetry build
```

Run tests through the Makefile targets (they also run formatting first):

```bash
# Unit tests only (excludes integration + authenticated)
make unittest

# Integration tests (Docker required)
make integration

# Authenticated tests (Docker required, optional BOINC_PROJECT_KEY)
make authenticated

# Full test suite
make test
```

Run a single test directly with pytest:

```bash
# Single test function
poetry run pytest tests/projects/test_projects.py::test_can_attach_to_project -vv

# Single integration test
poetry run pytest tests/integration/test_boinc_client.py::test_results -m integration -vv
```

Coverage workflow used by this repo:

```bash
make coverage
```

Formatting commands:

```bash
make fmt
make fmtxml
```

Style checks (no dedicated lint target; run tools in check mode):

```bash
poetry run black --check src/ tests/
poetry run isort --profile=black --check-only src/ tests/
```

## High-level architecture

- `src/boinc_client/boinc_client.py` exposes the `Boinc` facade class. Public methods are thin delegations to domain modules (`messages.py`, `projects.py`, `status.py`, etc.).
- `src/boinc_client/clients/rpc_client.py` is the transport layer. It manages socket connection/authentication to BOINC RPC, wraps outgoing payloads in `<boinc_gui_rpc_request>...</boinc_gui_rpc_request>\003`, reads until `\003`, and strips `<boinc_gui_rpc_reply>` wrappers in `make_request`.
- Domain modules in `src/boinc_client/*.py` follow the same pipeline:
  1. Build XML request strings for BOINC RPC
  2. Call `RpcClient.make_request`
  3. Parse XML with `xmltodict.parse` (often with `force_list`)
  4. Load into marshmallow schemas under `src/boinc_client/models/`
- Marshmallow schemas are the canonical response normalization layer. They convert variable RPC XML shapes into consistent Python dict structures returned by the public API.
- Tests are split by marker and runtime dependency:
  - Unit tests: mock `RpcClient.make_request`
  - `integration`: real BOINC Docker container via `testcontainers`
  - `authenticated`: integration flow requiring BOINC RPC password/auth operations

## Key codebase conventions

- Keep `Boinc` methods as wrappers; put operation logic in domain modules (`projects.py`, `status.py`, etc.), not in `boinc_client.py`.
- New RPC operations should return normalized dicts by introducing/updating marshmallow schemas rather than returning raw `xmltodict` output.
- Use `xmltodict.parse(..., force_list=...)` when BOINC may return one-or-many nodes; this prevents shape drift between single-item and multi-item responses.
- Prefer shared helpers in `models/helpers.py` (`flatten_data`, `normalise_none_to_list`, `create_indexes`, `set_bools`, etc.) for schema transformations instead of duplicating normalization logic.
- Pre/post-load transform methods in schemas use alphabetical prefixes (`_a_`, `_b_`, `_c_`) to keep transformation order explicit and stable.
- Generic command responses use `GenericResponse` (`{"success": bool, "error": ...}`), with success inferred from presence of `<success/>`.
- Integration fixtures in `tests/integration/conftest.py` standardize container setup (`boinc/client`, port `31416`, `--allow_remote_gui_rpc`) and should be reused for new integration/authenticated tests.

## MCP server guidance

- Use GitHub MCP tools for repository and CI workflows instead of manual API/scraping:
  - PR/issue context: `list_pull_requests`, `pull_request_read`, `list_issues`, `issue_read`
  - CI diagnostics: `actions_list` (runs/jobs/artifacts) and `get_job_logs` for failed jobs
  - Commit/file inspection during reviews: `list_commits`, `get_commit`, `get_file_contents`
- Prefer MCP read/list/search tools when triaging CI failures or preparing release-related changes, because this repository depends on GitHub Actions (`.github/workflows/pull-request.yml`, `test-and-release.yml`) for validation and publishing.
