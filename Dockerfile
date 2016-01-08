FROM logstash:2.0.0-1
MAINTAINER Matt Kimber <matt.kimber@collinsongroup.com>

COPY src /create_exchange
COPY config /etc/exchanges

RUN cd /create_exchange \
    && apt-get update \
    && apt-get install -y python-pip \
    && pip install -r requirements.txt \
    && apt-get remove -y python-pip \
    && apt-get clean
    
ENV RABBIT_HOST=localhost

ENTRYPOINT ["/create_exchange/start.sh"]
CMD ["logstash", "agent"]