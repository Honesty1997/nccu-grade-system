.PHONY: dev-up dev-build dev-down dev-restart shell clean
CONTAINER_NAME = mysite-web
DB_NAME = mysite-db

dev-up:
	docker-compose -f ./docker/docker-compose.yml up
dev-build:
	docker-compose -f ./docker/docker-compose.yml build
dev-down:
	docker-compose -f ./docker/docker-compose.yml down
dev-restart:
	docker-compose -f ./docker/docker-compose.yml restart
shell:
	docker exec -it ${CONTAINER_NAME} bash
dbshell:
	docker exec -it ${DB_NAME} bash
clean:
	rm -rf .docker-assets/db/data/*
test:
	python manage.py test -v 2
