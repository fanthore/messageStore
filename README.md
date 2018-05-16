# RMEssageStore

Simple python project to store owtracks location data to sqlite DB

This project is not dry yet. Use at your own risks

## Getting Started

You will need a working MQTT mosquitto broker and owntracks installed on one client.

### Prerequisites

MQTT Mosquitto
owtracks
python
paho-mq
sqlite3

## Starting up

```
$ python init.py
$ ls owntracks.db
owntacks.db
$ sqlite owntracks.db .dump
```

## License

This project is licensed under GPL V3

