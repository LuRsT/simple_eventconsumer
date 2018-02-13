FROM alpine:latest

RUN apk --update upgrade && apk add python3-dev build-base

COPY . ./

RUN pip3 install -r requirements.txt

CMD "./entrypoint.sh"
