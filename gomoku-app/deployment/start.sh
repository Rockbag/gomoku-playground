#!/bin/bash

set euo -pipefail

docker-compose down
docker-compose -v rm -y

bash build.sh
docker-compose up -d

