PR=poetry run python manage.py

dev:
	$(PR) runserver

test:
	$(PR) test lists

fun-test:
	$(PR) test functional_tests

migrate:
	$(PR) makemigrations
	$(PR) migrate

shell:
	$(PR) shell_plus --ipython
