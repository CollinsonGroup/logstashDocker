#!/bin/bash
set -e
python /create_exchange/createExchanges.py /etc/exchanges/rabbit.json

exec /docker-entrypoint.sh "$@"