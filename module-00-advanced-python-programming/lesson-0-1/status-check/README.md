# status-check

Request a web address and print its HTTP status code.

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

uv installs the Python version listed in `.python-version` (3.13) if it is missing.

## Set up

```sh
uv sync --locked
```

## Run

```sh
uv run --locked status-check
uv run --locked status-check https://example.com
```

## Develop

```sh
uv run ruff check
uv run ruff format
```
