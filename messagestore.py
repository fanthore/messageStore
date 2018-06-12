#!/usr/bin/python

from store_to_db import mqtt_device
import paho.mqtt.client as mqttClient
import time

 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

 
def on_message(client, userdata, message):
    print message.topic + message.payload
    mqtt_device(message.topic, message.payload)

 
Connected = False   #global variable for the state of the connection
 
broker_address= "4ytm.com"
port = 1883
 
client = mqttClient.Client("Python")
client.on_connect= on_connect
client.on_message= on_message
 
client.connect(broker_address, port=port) 
 
client.loop_start()
 
while Connected != True:
    time.sleep(0.1)
 
client.subscribe("owntracks/#")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()
