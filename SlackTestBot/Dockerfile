

FROM python:3.7-alpine 

ADD ./ SlackTestBot 
WORKDIR /SlackTestBot

ENV PYTHONPATH /

RUN sed -i 's/dl-cdn.alpinelinux.org/uk.alpinelinux.org/' /etc/apk/repositories
RUN sed -i 's/http/https/' /etc/apk/repositories

RUN apk add --no-cache python3-dev && \
    pip install -r requirements.txt

RUN apk --no-cache add curl zip

ENTRYPOINT ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
