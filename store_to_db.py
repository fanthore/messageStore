
import json
import sqlite3
import datetime

DB_Name =  "owntracks.db"

# Database Manager Class

class DatabaseManager():
    def __init__(self):
        self.conn = sqlite3.connect(DB_Name)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()
        return
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
    
# Function to push Device Location Data into Database

def mqtt_device(Topic, jsonData):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    json_Dict = json.loads(jsonData)

    tid = json_Dict.get('tid', 'ukn')
    top = Topic
    acc = json_Dict.get['acc', 999]
    bat = json_Dict.get['batt', 101]
    lat = json_Dict.get['lat', 0.0]
    lon = json_Dict.get['lon', 0.0]
    tst = json_Dict.get['tst', 1]
    
    #Push into DB Table
    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record("insert into MQTT_devices (top, tid, acc, bat, lat, lon, tst, now) values (?,?,?,?,?,?,?,?)",[top, tid, acc, bat, lat, lon, tst, now])
    del dbObj
    #print "Inserted Device location Data to Database."
    #print ""

