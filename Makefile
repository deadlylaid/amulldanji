shell:
	python amulldanji/manage.py shell_plus

clean:
	find ./ -type f -name "\.*swp" -delete

migrate:
	python amulldanji/manage.py makemigrations users items
	python amulldanji/manage.py migrate
