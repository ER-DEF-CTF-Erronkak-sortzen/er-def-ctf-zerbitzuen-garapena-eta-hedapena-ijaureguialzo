#!/usr/bin/env bash

docker-compose -f "$SERVICES_PATH/vulnerable/docker-compose.yml" up -d --build
