migration:
	alembic revision --autogenerate -m "${message}"

upgrade:
	alembic upgrade head

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-restart:
	docker-compose down
	docker-compose up -d


