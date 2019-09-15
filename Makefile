.PHONY: help init update clean clean-build clean-docs clean-pyc lint test test-all coverage docs release sdist

help:
	@echo "help - display this message"
	@echo "init - create the pipenv and install dependencies"
	@echo "update - update the dependencies"
	@echo "clean - remove temporary files"
	@echo "clean-build - remove build artifacts"
	@echo "clean-docs - remove docs artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

init:	
	pipenv --three
	pipenv install --dev --skip-lock
	pipenv install -r requirements.txt
	pipenv run setup.py develop

update:
	pipenv update
	pipenv lock -r

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	pipenv run flake8 --output-file=.flake8.txt typical tests 	

test:
	pipenv run py.test --junitxml=.tests_report.xml

test-all:
	pipenv run tox

coverage:
	pipenv run py.test --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=requests tests

release: clean
	pipenv run python setup.py sdist upload
	pipenv run python setup.py bdist_wheel upload

sdist: clean
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel upload
	ls -l dist
