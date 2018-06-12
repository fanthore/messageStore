# messageStore

Simple python project to store owntracks location data to sqlite DB


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
  tst integer,
  now text);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('MQTT_devices',3121);
COMMIT;


```
## Running it

Quick way :

```
$ python messagestore.py
Connected to broker
```

Better way : 

Better run this as a service using systemctl as you will have better logging, recovery, etc. Refer to **messagestore.service** file to create your service. There are thousands of how-to out there. This one works : [https://www.devdungeon.com/content/creating-systemd-service-files](https://www.devdungeon.com/content/creating-systemd-service-files)

## License

This project is licensed under GPL V3

