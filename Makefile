APPLICATION_MODULE=gitanalysis
TEST_MODULE=$(APPLICATION_MODULE)_tests

# @see http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.DEFAULT_GOAL := help
.PHONY: help
help: ## provides cli help for this makefile (default)
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: dist
dist:
	. venv/bin/activate; python setup.py sdist

.PHONY: tests
tests: tests_units tests_acceptances ## run automatic tests

.PHONY: tests_units
tests_units: ## run only unit tests
	. venv/bin/activate; python -u -m unittest discover "$(TEST_MODULE)/units"

.PHONY: tests_acceptances
tests_acceptances: ## run only acceptance tests
	. venv/bin/activate; python -u -m unittest discover "$(TEST_MODULE)/acceptances"

.PHONY: tox
tox: ## run tests described in tox.ini
	. venv/bin/activate; tox

.PHONY: lint
lint: ## run pylint
	. venv/bin/activate; pylint --rcfile=.pylintrc $(APPLICATION_MODULE)

.PHONY: coverage
coverage: coverage_run coverage_html ## output the code coverage in htmlcov/index.html

coverage_run :
	. venv/bin/activate; coverage run -m unittest discover $(TEST_MODULE)

coverage_html:
	. venv/bin/activate; coverage html
	@echo "$ browse htmlcov/index.html"

.PHONY: clean
clean : ## remove all transient directories and files
	rm -rf dist
	rm -rf venv
	rm -f .coverage
	rm -rf *.egg-info
	rm -f MANIFEST
	find -name __pycache__ -print0 | xargs -0 rm -rf

.PHONY: freeze
freeze: ## freeze the dependencies version in requirements.txt for information
	. venv/bin/activate; pip freeze | @grep -v "$(APPLICATION_MODULE)" > requirements.txt

.PHONY: install_requirements_dev
install_requirements_dev: venv ## install pip requirements for development
	. venv/bin/activate; pip install -r requirements_dev.txt

.PHONY: venv
venv: ## build a virtual env for python 3 in ./venv
	virtualenv venv -p python3
	@echo "\"source venv/bin/activate\" to activate the virtual env"
