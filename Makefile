shell:
	python amulldanji/manage.py shell_plus

clean:
	find ./ -type f -name "\.*swp" -delete

migrate:
	python amulldanji/manage.py makemigrations items users
	python amulldanji/manage.py migrate
