#!/bin/bash
set -e
echo Configuring Exchanges
python /configScripts/createExchanges.py /etc/exchanges/rabbit.json

echo Configuring Logstash
python /configScripts/createLogstashConfig.py

/docker-entrypoint.sh $@
