#!/usr/bin/env python
import os
import sys
from quik import FileLoader

elasticsearchHost = os.getenv('ELASTICSEARCH_HOST', 'elasticsearch')
elasticsearchPort = os.getenv('ELASTICSEARCH_PORT', "9200")

templateValues = {
    'rabbitHost': os.getenv('RABBIT_HOST', "localhost"),
    'rabbitPort': os.getenv('RABBIT_PORT', "5672"),
    'rabbitUsername': os.getenv('RABBIT_USERNAME', "guest"),
    'rabbitPassword': os.getenv('RABBIT_PASSWORD', "guest"),
    'rabbitExchange': os.getenv('RABBIT_EXCHANGE', 'client_exchange'),
    'rabbitQueue': os.getenv('RABBIT_QUEUE', 'logstash'),
    'elasticsearchHost': elasticsearchHost + ':' + elasticsearchPort
    }

def main(argv):
    baseFolder = argv[0] if len(argv) > 0 else '/etc/exchanges'
    outputFilePath = argv[1] if len(argv) > 1 else "/etc/logstash/conf.d/logstash.conf"

    # Format template with values from environment
    loader = FileLoader(baseFolder)
    template = loader.load_template('logstash.conf.tmpl')
    renderedTemplate = template.render(templateValues,
                          loader=loader).encode('utf-8')

    # Save into logstash folder
    with open(outputFilePath, "w") as text_file:
        text_file.write("{0}".format(renderedTemplate))

if __name__ == "__main__":
   main(sys.argv[1:])
