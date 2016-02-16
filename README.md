# Logstash with RabbitMQ Exchange Creation

This is a container intended for use in opinionated Logstash installs where Logstash connects to a pre-existing Rabbit install, creating an exchange and queue to listen on.
By default Logstash can create a queue and bind it to an existing exchange but is not capable of creating the topic exchange. This container allows creating exchanges as well
based on a JSON configuration.

## Configuration

### Rabbit Host

The container uses environment variables to configure RabbitMQ:

| Variable    | Meaning |
|-------------|---------|
| RABBIT_HOST | The RabbitMQ host (e.g. 192.168.0.1) |

At present, the default Rabbit ports are used.

### Creating Exchanges

To define exchanges, you will need to supply a rabbit.json file by adding a volume definition
for **/etc/exchanges/rabbit.json**. It is only the **rabbit.json** file that's required. Other files are in that folder so if you mount all of it, the container will likely fail.

An example rabbit.json file is given in the ```./examples``` folder. Typically a configuration takes
the following form:

```json
{
   	"exchanges": [
		{
			"name": "exchange_name",
            ...
		}
    ]
}
```

Allowed variables are as follows:

| Variable   | Meaning                                        |
|------------|------------------------------------------------|
| name       | Name of the exchange to create.                |
| vhost      | vhost the exchange is created under.           |
| type       | Type of exchange, e.g. "fanout", "direct" etc. |
| durable    | Whether the exchange is persisted to disk      |
| internal   | Whether the exchange is a Rabbit internal one  |

These are essentially the same options as Rabbit's own queue definition mechanism.

## Creating the Container

To build the container, use Docker build:

```bash
> docker build -t collinsongroup/logstash .
```

## Running the Container

The container takes several environment variables to configure it for use:

| Variable           | Meaning                                        | Default           |
|--------------------|------------------------------------------------|-------------------|
| RABBIT_HOST        | Hostname or IP for the Rabbit instance         | localhost         |
| RABBIT_PORT        | Port Rabbit is listening on                    | 5672              |
| RABBIT_EXCHANGE    | Name of the Exchange to use                    | client_operations |
| RABBIT_QUEUE       | Name of the Rabbit queue to use                | logstash          |
| RABBIT_USERNAME    | User to connect to Rabbit with                 | guest             |
| RABBIT_PASSWORD    | Password for Rabbit user                       | guest             |
| ELASTICSEARCH_HOST | Hostname or IP of the Elasticseach instance    | elasticseach      |
| ELASTICSEARCH_PORT | Port Elasticsearch listens on                  | 9200              |

You can specify the vaslues you want to change as part of the **Docker Run** command:

```bash
> docker run -d -e RABBIT_HOST=10.10.1.2 -e RABBIT_PORT=9999 -v $(pwd)/examples:/etc/exchanges --name myLogstash collinsongroup/logstash
```
