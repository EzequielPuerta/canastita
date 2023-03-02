migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

requirements:
	pip install -r requirements.txt

run:
	make migrate
	python manage.py runserver

shell:
	python manage.py shell

superuser:
	python manage.py createsuperuser

test:
	pytest -s --durations=10 --create-db

coverage:
	coverage html
	@echo
	@echo "Generating coverage report..."
	@printf '**** Code Coverage Total: \033[30;48;5;82m  '
	@echo -n $(shell coverage report | grep TOTAL | awk '{print $$4}')
	@printf '  \033[0m **** '
	@echo

clean:
	rm -Rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} \+