clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
	rm -fr cover
	rm .coverage

setup:
	pip install -r requirements.txt
	pip install -r requirements_test.txt
	tox -r

tests:
	tox

jupyter:
	@rm -fr dist/*
	@python setup.py sdist
	@cp -f dist/paa191t1-0.0.0.tar.gz /Users/arnour.sabino/DockerVolumes/jupyter/paa191t1-0.0.0.tar.gz