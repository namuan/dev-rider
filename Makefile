export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ;               # no need for @

setup: ## Setup virtual environment and install dependencies
	echo "Run the following commands to install required dependencies"
	echo "python3 -m venv venv"
	echo "source venv/bin/activate"
	echo "pip install -r requirements/dev.txt"
	echo "Once everything is installed, 'make run' to run the application"

release: ## Step to prepare a new release
	echo "Instructions to prepare release"

venv: ## Load virtualenv
	source venv/bin/activate

clean: ## Clean package
	rm -rf build dist

lint: ## Runs Flake8 for linting
	flake8 app

reset: ## Re-initiates virtualenv
	rm -rf venv
	python3 -m venv venv
	./venv/bin/python3 -m pip install -r requirements/dev.txt

deps: ## Reinstalls dependencies
	./venv/bin/python3 -m pip install -r requirements/dev.txt

package: clean ## Rebuilds venv and packages app
	./venv/bin/python3 setup.py bdist_app

docs: clean ## Build docs
	./venv/bin/python3 setup.py build_docs

uic: res ## Converts ui files to python
	for i in `ls resources/views/*.ui`; do FNAME=`basename $${i} ".ui"`; ./venv/bin/pyuic5 $${i} > "app/generated/$${FNAME}_ui.py"; done

res: venv ## Generates and compresses resource file
	./venv/bin/pyrcc5 -compress 9 -o app/generated/resources_rc.py resources/resources.qrc

run: ## Runs the application
	export PYTHONPATH=`pwd`:$PYTHONPATH && python app/__main__.py

icns: ## Generates icon files from svg
	echo "Run ./mk-icns.sh resources/icons/app.svg app"

.PHONY: help
.DEFAULT_GOAL := setup

help: Makefile
	echo
	echo " Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo