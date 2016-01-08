#!/usr/bin/env python
import pika
import sys
import json
import os

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

def addedExchange():
    print "Added Exchange"

rabbitHost = os.getenv('RABBIT_HOST', "localhost")

def main(argv):
    filename = argv[0] if len(argv) > 0 else 'rabbit.json'

    # Connect to rabbit
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitHost))
    channel = connection.channel()

    with open(filename) as data_file:
        data = json.load(data_file)

    # Loop and add exchanges
        for exchangeId in range(len(data["exchanges"])):
            exchange = data["exchanges"][exchangeId]

            channel.exchange_declare(
                                    exchange=exchange["name"],
                                    exchange_type=exchange["type"],
                                    durable=str2bool(exchange["durable"]),
                                    auto_delete=False,
                                    internal=str2bool(exchange["internal"]))

if __name__ == "__main__":
   main(sys.argv[1:])