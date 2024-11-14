#!/usr/bin/env bash

docker stop vulnerable_ssh_1
docker stop vulnerable_web_1
docker rm vulnerable_ssh_1
docker rm vulnerable_web_1