import sensor.distance_sensor
import dhbw_iot_csv.csv_writer
import threading
import time
from mqtt.mqtt_Com import mqttCommunication as mqtt
from mqtt import pubsub 

class sensorThread (threading.Thread):
    def __init__(self, namen):
        threading.Thread.__init__(self)
        self.namen=namen

    def run(self):
        print("Starte Thread mit dem Namen:",self.namen)
        instance_pubsub= pubsub.Pubsub()
        instanz= sensor.distance_sensor.DistanceSensor(instance_pubsub)
        instanz.read_value()

    
class receiveThread(threading.Thread):
    def __init__(self,namen):
        threading.Thread.__init__(self)
        self.namen=namen
    def run(self):
        print("Starte Thread mit dem Namen:", self.namen)
        
        ps= pubsub.Pubsub()
        communicator= mqtt(ps)
        



t1= sensorThread("iot-sensor-Thread")
t1.start()

t2= receiveThread("iot-receive-Alert-Thread")
t2.start()



