create-dir:
	mkdir sql-data

docker-run:
	docker run --rm -d \
		-p 5432:5432 \
		--name url-shortr-db \
		-e POSTGRES_PASSWORD=postgres \
		-e PGDATA=/var/lib/postgresql/data/pgdata \
		-v $(pwd)/sql-data/:/var/lib/postgresql/data \
		postgres:14-alpine

podman-run:
	podman run --rm -d \
		-p 5432:5432 \
		--name url-shortr-db \
		-e POSTGRES_PASSWORD=postgres \
		-e PGDATA=/var/lib/postgresql/data/pgdata \
		-v $(pwd)/sql-data/:/var/lib/postgresql/data \
		postgres:14-alpine
