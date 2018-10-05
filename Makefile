.PHONY: dev-up dev-build dev-down dev-restart shell
CONTAINER_NAME = mysite-web

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
clean:
	rm -rf .docker-assets/db/data/*
