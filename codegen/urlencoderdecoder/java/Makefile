export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ;               # no need for @

setup: ## Setup application
	echo "Steps required to setup sample application"

build: ## Build application
	echo "Steps required to build sample application"

test: ## Test application
	echo "Steps required to test sample application"

.PHONY: help
.DEFAULT_GOAL := setup

help: Makefile
	echo
	echo " Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo