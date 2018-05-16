# messageStore

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
-- Loading resources from /home/fanthore/.sqliterc

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE MQTT_devices (
  id integer primary key autoincrement,
  top text,
  tid text,
  acc integer,
  bat integer,
  lat real,
  lon real,
  tst integer
, now text);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('MQTT_devices',0);
COMMIT;

```
## Running it


```
$ python connect.py
Connected to broker
```

## License

This project is licensed under GPL V3

