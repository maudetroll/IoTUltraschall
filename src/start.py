import sensor.distance_sensor
import csv_123.csv_writer
import threading
import time
import mqtt.mqtt_Com

class sensorThread (threading.Thread):
    def __init__(self, namen):
        threading.Thread.__init__(self)
        self.namen=namen

    def run(self):
        print("Starte Thread mit dem Namen:",self.namen)
        instanz= sensor.distance_sensor.DistanceSensor()
        p=instanz.read_value()
        #time.sleep(10)

    
class receiveThread(threading.Thread):
    def __init__(self,namen):
        threading.Thread.__init__(self)
        self.namen=namen
    def run(self):
        print("Starte Thread mit dem Namen:", self.namen)
        time.sleep(10)



t1= sensorThread("iot-sensor-Thread")
t1.start()

t2= receiveThread("iot-receive-Thread")
t2.start()

communication= mqtt.mqtt_Com.mqttCommunication("localhost")
communication.connectToMQTT()
print(communication.on_connect)
print(communication.on_message)

