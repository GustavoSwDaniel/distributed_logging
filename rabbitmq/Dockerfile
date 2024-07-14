FROM rabbitmq:3.13.0-management
RUN apt-get update && apt-get install -y wget
RUN rabbitmq-plugins enable rabbitmq_management rabbitmq_stream rabbitmq_stream_management
EXPOSE 5672 15672 5552
CMD ["rabbitmq-server"]