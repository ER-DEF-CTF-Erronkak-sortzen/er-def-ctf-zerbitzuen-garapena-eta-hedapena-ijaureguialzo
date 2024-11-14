#!/usr/bin/env bash

docker rm -fv vulnerable-phpmyadmin-1
docker rm -fv vulnerable-web-1
docker rm -fv vulnerable-db-1
docker volume rm -f vulnerable_mariadb-data
docker network rm -f vulnerable_default
