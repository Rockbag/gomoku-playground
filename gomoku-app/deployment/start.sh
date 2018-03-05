#!/bin/bash

set euo -pipefail

docker-compose down
docker-compose rm -v -y

bash build.sh
docker-compose up -d

