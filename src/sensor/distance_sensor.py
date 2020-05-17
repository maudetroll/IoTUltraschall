import time
import RPi.GPIO as GPIO
import datetime
import dhbw_iot_csv.csv_writer
import alerts.alert_service as Alarm
import mqtt.mqtt_Com as mqtt


class DistanceSensor:
    def __init__(self, pubsub):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.Trigger_AusgangsPin = 17
        self.Echo_EingangsPin = 27
        GPIO.setup(self.Trigger_AusgangsPin, GPIO.OUT)
        GPIO.setup(self.Echo_EingangsPin, GPIO.IN)
        GPIO.output(self.Trigger_AusgangsPin, False)
        self.sleeptime = 1
        self.pubsub = pubsub
        self.writer = dhbw_iot_csv.csv_writer.CsvWriter()
        pass
# In dieser Funktion werden die Sensordaten ausgelesen und per Funktionsaufruf an die CSV Klasse weitergegeben
# Ebenso wird per Funktionsaufruf die Alert-Klasse angesprochen, welche Alarme versendet 
    def read_value(self):
        try:
            while True:
                GPIO.output(self.Trigger_AusgangsPin, True)
                time.sleep(0.00001)
                GPIO.output(self.Trigger_AusgangsPin, False)

# Ermittlung der Einschaltzeit und Ausschaltzeit 
                EinschaltZeit = time.time()
                while GPIO.input(self.Echo_EingangsPin) == 0:
                    EinschaltZeit = time.time()

                while GPIO.input(self.Echo_EingangsPin) == 1:
                    AusschaltZeit = time.time()
                Dauer = AusschaltZeit - EinschaltZeit
                Abstand = (Dauer * 34300) / 2
                Abstand = format((Dauer * 34300) / 2, '.2f')
                print("Der Abstand beträgt:", Abstand, ("cm"))
                print("************************")
# Konvertierung in das ISO 8601-Format laut https://www.it-swarm.dev/de/python/iso-zeit-iso-8601-python/968377307/                 
                timestamp = datetime.datetime.now().isoformat()

                eintragJSON = {
                    "sensorId": "Ultraschall Sensor KY-050",
                    "timestamp": timestamp,
                    "distance": Abstand,
                    "unit": "cm"
                }
# der CSV Writer erhält die Daten, welche dieser in die CSV-Datei schreibt
                self.writer.format_line(eintragJSON)
# Hiermit werden die Daten als JSON an MQTT weitergegeben und versandt
                mqtt.mqttCommunication(
                    self.pubsub).publishData(eintragJSON)

# sofern der Abstand kleiner als der Mindestabstand ist, so wird ein Alarm ausgesandt
# dies erfolgt in der AlertService-Klasse
                instance= Alarm.AlertService(self.pubsub)
                if(float(Abstand) < float(instance.minimumdistance)):
#                   alarm = Alarm(self.pubsub)
                    instance.on_distance_threshold_passed(Abstand)

                time.sleep(self.sleeptime)


# Das Mapping für die GPIO Pins resetet
        except KeyboardInterrupt:
            GPIO.cleanup()
    pass
