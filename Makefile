dev:
	poetry run python manage.py runserver

test:
	poetry run python manage.py test

fun-test:
	poetry run python functional_tests.py


