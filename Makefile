SHELL := /bin/bash

.PHONY: lint
lint: ## Run the linters
	flake8 .
