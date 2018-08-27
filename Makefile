CONTAINER_NAME = mysite-web

dev-up:
	docker-compose -f ./docker/docker-compose.yml up
dev-build:
	docker-compose -f ./docker/docker-compose.yml build
dev-down:
	docker-compose -f ./docker/docker-compose.yml down

shell:
	docker exec -it ${CONTAINER_NAME} bash