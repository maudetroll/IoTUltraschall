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
        Trigger_AusgangsPin = 17
        Echo_EingangsPin = 27
        GPIO.setup(Trigger_AusgangsPin, GPIO.OUT)
        GPIO.setup(Echo_EingangsPin, GPIO.IN)
        GPIO.output(Trigger_AusgangsPin, False)
        self.sleeptime = 1
        self.pubsub = pubsub
        pass

    def read_value(self):
        writer = dhbw_iot_csv.csv_writer.CsvWriter()
        GPIO.setmode(GPIO.BCM)
        Trigger_AusgangsPin = 17
        Echo_EingangsPin = 27
        GPIO.setup(Trigger_AusgangsPin, GPIO.OUT)
        GPIO.setup(Echo_EingangsPin, GPIO.IN)
        GPIO.output(Trigger_AusgangsPin, False)

        try:
            while True:
                GPIO.output(Trigger_AusgangsPin, True)
                time.sleep(0.00001)
                GPIO.output(Trigger_AusgangsPin, False)

                EinschaltZeit = time.time()
                while GPIO.input(Echo_EingangsPin) == 0:
                    EinschaltZeit = time.time()

                while GPIO.input(Echo_EingangsPin) == 1:
                    AusschaltZeit = time.time()

                Dauer = AusschaltZeit - EinschaltZeit
                Abstand = (Dauer * 34300) / 2

                Abstand = format((Dauer * 34300) / 2, '.2f')
                print("Der Abstand beträgt:", Abstand, ("cm"))
                print("------------------------------")
                timestamp = datetime.datetime.now().isoformat()
                eintragJSON = {
                    "sensorId": "Ultraschall Sensor KY-050",
                    "timestamp": timestamp,
                    "distance": Abstand,
                    "unit": "cm"
                }
                writer.format_line(eintragJSON)
                mqtt.mqttCommunication(
                    self.pubsub).publishData(eintragJSON)

                if(float(Abstand) < float(Alarm.AlertService(self.pubsub).minimumdistance)):
                    alarm = Alarm.AlertService(self.pubsub)
                    alarm.on_distance_threshold_passed(Abstand)
                    print("Abstand außerhalb des Messbereich")
                    print("------------------------------")

                time.sleep(self.sleeptime)


# Aufraeumarbeiten nachdem das Programm beendet wurde
        except KeyboardInterrupt:
            GPIO.cleanup()
    pass
