#!python3
import paho.mqtt.client as mqtt
import time
import json
from config.configuration import Configuration 
import alerts.alert_service as AService
import logging

class mqttCommunication():

# im Konstruktor wird MQTT definiert
    def __init__(self,pubsub):

        config= Configuration()
        self.broker= config.config["broker_host"]
        self.port= config.config["broker_port"]
        logging.info(self.broker, self.port)

        self.client = mqtt.Client()
        self.client.connect(self.broker,self.port)
        self.client.on_message= self.on_message
        self.client.subscribe(config.config["config_topic"],qos=1)
        self.client.loop_start()

        self.pubsub= pubsub
        self.pubsub.on_connect= self.on_connect
        self.pubsub.on_message= self.on_message
        pass

# Diese Funktion setzt den Payload, welcher über das config_topic versandt wurde, als minimalen Abstand
    def on_message(self,client, userdata, msg):
        AService.AlertService(self.pubsub).set_alert_threshold(float(msg.payload), "cm")
        pass

    def on_connect(self,client,userdata,flags,rc):
        print("Connected with result code", str(rc))        
        self.client.subscribe("")
        pass
# Diese Funktion sendet die Messdaten, die Einheit, die Sensorbezeichnung und den Zeitstempel an das entsprechende Topic in dem Falle distances
    def publishData(self,dict):
        config= Configuration()
        self.client.publish(config.config["data_topic"], json.dumps(dict))
        pass 

# Diese Funktion sendet die Alarme via MQTT an das entsprechende Topic, in dem Falle alert_distance
    def sendAlarm(self,abstand):
        config= Configuration()
        alert= AService.AlertService(self.pubsub)
        message= "Alarm, wir haben den Schwellwert von:",alert.minimumdistance," mit",float(abstand),alert.unit," unterschritten"
        self.client.publish(config.config["alert_topic"],str(message))





