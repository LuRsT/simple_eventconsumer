# Simple Eventconsumer

This is the simplest python event consumer using eventstore I could think of.


## Requirements:

- docker-compose (and docker of course)


## How to Run?

- In a terminal run `docker-compose up`
- Once it's running, in another terminal, run:

```sh
python send_test_event.py "Gil"
```

You should see in the docker-compose logs the following:

```
eventconsumer_1  | WARNING:root:Hi Gil
```
