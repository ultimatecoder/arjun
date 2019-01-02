SHELL := /bin/bash

.PHONY: build
build: ## Prepares a development build of the project
	pip install --user pipenv
	cd api; pipenv install --dev

.PHONY: lint
lint: ## Run the linters
	pipenv run flake8 . --exclude=migrations

.PHONY: test
test: ## Run all level of tests
	pipenv run python api/manage.py test api


.PHONY: run
run: ## Run the app
	cd api; pipenv run python manage.py makemigrations
	cd api; pipenv run python manage.py migrate
	cd api; pipenv run python manage.py runserver

.PHONY: docker
docker: ## Boostrap project using docker compose
	docker-compose up --build

.PHONY: help
help: ## Print this message and exit.
	@printf "Makefile for developing and testing Arjun.\n"
	@printf "Subcommands:\n\n"
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%s\033[0m : %s\n", $$1, $$2}' $(MAKEFILE_LIST) \
		| sort \
		| column -s ':' -t
