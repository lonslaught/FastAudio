.DEFAULT_GOAL := help

lint:  ## Run ruff & mypy linter
	uv run ruff check . --select I && uv run mypy app/ --explicit-package-bases
pre-commit:  ## Run ruff formatter
	uv run ruff check . --select I --fix

local:  ## Build & Run LOCAL stage
	docker compose -f deploy/local/compose.yaml up --build

tree:  ## Show tree project structure
	tree . -I .venv -I .ruff_cache -I data -I __pycache__

help:  ## Show this help message
	@echo "Usaage make [command]"
	@echo ""
	@echo "Commands:"
	@grep -E '[a-zA-Z0-9_-]+:.*?##.*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf " %-20s %s\n", $$1, $$2}'
