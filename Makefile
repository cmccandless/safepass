all: build test upload

clean:
	- rm -rf build/ dist/ *.egg-info/

build:
	- python3 setup.py sdist bdist_wheel

test:
	@ echo 'No tests configured'

upload-test:
	- twine upload -r testpypi dist/*

upload:
	- twine upload -r pypi dist/*
