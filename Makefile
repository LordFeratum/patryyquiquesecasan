all: build

build:
	docker-compose up --build -d gunicorn

.PHONY: build
