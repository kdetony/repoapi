FROM alpine:latest

RUN apk -U upgrade && apk add --no-cache python3 py3-pip

WORKDIR /app 

COPY api.* server.* requirements.txt  /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3","api.py"]
