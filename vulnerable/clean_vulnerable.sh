#!/usr/bin/env bash

docker rm -fv vulnerable_phpmyadmin_1
docker rm -fv vulnerable_web_1
docker rm -fv vulnerable_db_1
docker volume rm -f vulnerable_mariadb-data
docker network rm vulnerable_default
