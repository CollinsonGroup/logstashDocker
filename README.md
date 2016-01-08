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
for /etc/exchanges

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

## Creating the container

To build the container, use Docker build:

```bash
> docker build -t collinsongroup/logstash .
```

