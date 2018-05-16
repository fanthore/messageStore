import sqlite3

DB_Name =  "owntracks.db"

TableSchema="""
drop table if exists MQTT_devices ;
create table MQTT_devices (
  id integer primary key autoincrement,
  top text,
  tid text,
  acc integer,
  bat integer,
  lat real,
  lon real,
  tst integer,
  now text
);


"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()
