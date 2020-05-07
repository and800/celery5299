#!/usr/bin/env bash
set -eo pipefail

docker-compose up -d
docker-compose exec app python cli.py 1
docker-compose logs -f
