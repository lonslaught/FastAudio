.DEFAULT_GOAL := help

local:  ## Build & Run LOCAL stage
	docker compose -f deploy/local/compose.yaml up --build

tree:  ## Show tree project structure
	tree . -I .venv -I .ruff_cache -I data -I __pycache__