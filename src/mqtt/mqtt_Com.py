#!python3
import paho.mqtt.client as mqtt
import time
import json
from config.configuration import Configuration 

class mqttCommunication():

    def __init__(self,broker):

        config= Configuration()
        self.broker= config.config["broker_host"]
        self.port= config.config["broker_port"]

        pass

    def connectToMQTT(self):

        self.client= mqtt.Client("iot_User_1")
        self.client.subscribe('distance')
        self.client.connect(self.broker,self.port,60)
        self.client.loop_forever()
        print("bin angekommen")
        
    def disconnectFromMQTT(self):
        pass
    
    def on_message(self,client, userdata, message):
        msg = str(message.payload.decode("utf-8"))
        print("message received: ", msg)
        print("message topic: ", message.topic)

    def on_connect(self,client,userdata,flags,rc):
        print("Connected with result code", str(rc))        
        self.client.subscribe("")



