export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ;               # no need for @

release: ## Step to prepare a new release
	echo "Instructions to prepare release"
	echo "Repo: dev-rider: Increment version in app/__init__.py"
	echo "Repo: dev-rider: Increment version in .travis.yml"
	echo "Commit - Preparing Release x.x.x"
	echo "Repo: dev-rider-osx: Increment version in .travis.yml"
	echo "Commit - Release x.x.x - MacOS"
	echo "Repo: dev-rider-win: Increment version in .appveyor.yml"
	echo "Commit - Release x.x.x - Windows"
	echo "Repo: dev-rider: Update Download Links in README.md"
	echo "Repo: deskriders.dev: Update Project Page with Download Links"

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean: clean-pyc ## Clean package
	rm -rf build dist

black: ## Runs black for code formatting
	black app --exclude generated

lint: black ## Runs Flake8 for linting
	flake8 app

setup: clean ## Re-initiates virtualenv
	rm -rf venv
	python3 -m venv venv
	./venv/bin/python3 -m pip install -r requirements/dev.txt
	echo "Once everything is installed, 'make run' to run the application"

deps: ## Reinstalls dependencies
	./venv/bin/python3 -m pip install -r requirements/dev.txt

package: clean ## Rebuilds venv and packages app
	./venv/bin/python3 -m pip install -r requirements/build.txt
	export PYTHONPATH=`pwd`:$PYTHONPATH && ./venv/bin/python3 setup.py bdist_app

uic: res ## Converts ui files to python
	for i in `ls resources/views/*.ui`; do FNAME=`basename $${i} ".ui"`; ./venv/bin/pyuic5 $${i} > "app/generated/$${FNAME}_ui.py"; done

res: ## Generates and compresses resource file
	./venv/bin/pyrcc5 -compress 9 -o app/generated/resources_rc.py resources/resources.qrc

run: ## Runs the application
	export PYTHONPATH=`pwd`:$PYTHONPATH && ./venv/bin/python3 app/__main__.py

runapp: ## Runs the packaged application
	./dist/DevRider.app/Contents/MacOS/app

icns: ## Generates icon files from svg
	echo "Run ./mk-icns.sh resources/icons/app.svg app"

newtool: ## Instructions for adding a new tool
	echo "cp resources/views/Base64EncoderWidget.ui resources/views/NewToolWidget.ui"
	echo "mkdir -vp app/tools/newtool"
	echo "cp app/tools/base64_encode_decoder.py app/tools/newtool/new_tool.py"
	echo "cp app/views/base64_encoder_widget.py app/views/newtool_widget.py"
	echo "mkdir -vp codegen/newtool"

.PHONY: help
.DEFAULT_GOAL := setup

help: Makefile
	echo
	echo " Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo