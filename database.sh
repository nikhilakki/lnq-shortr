# Copyright (c) 2022 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

#!/bin/zsh

mkdir sql-data
if [[ $1 == "docker" ]]; then
docker run --rm -d \
    -p 5432:5432 \
	--name url-shortr-db \
	-e POSTGRES_PASSWORD=postgres \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v $(pwd)/sql-data/:/var/lib/postgresql/data \
	postgres:14-alpine
elif [[ $1 == "podman" ]]; then
podman run --rm -d \
    -p 5432:5432 \
	--name url-shortr-db \
	-e POSTGRES_PASSWORD=postgres \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v $(pwd)/sql-data/:/var/lib/postgresql/data \
	postgres:14-alpine
fi