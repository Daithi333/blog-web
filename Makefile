.PHONY: test coverage coverage-html format

test:
	DJANGO_SETTINGS_MODULE=blogweb.settings.development PYTHONPATH=src pytest --verbose

coverage:
	DJANGO_SETTINGS_MODULE=blogweb.settings.development PYTHONPATH=src coverage run -m pytest && \
	coverage report -m

coverage-html:
	DJANGO_SETTINGS_MODULE=blogweb.settings.development PYTHONPATH=src coverage run -m pytest && \
	coverage html && \
	@echo "Open htmlcov/index.html in your browser to view the report."

format:
	ruff format src

run:
	ENV=development DB_HOST=localhost poetry run python src/manage.py runserver 0.0.0.0:8000
