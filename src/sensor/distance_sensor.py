import time
import RPi.GPIO as GPIO
import datetime
import csv_123.csv_writer
import alerts.alert_service

class DistanceSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM) 
        Trigger_AusgangsPin = 17
        Echo_EingangsPin    = 27
        GPIO.setup(Trigger_AusgangsPin, GPIO.OUT)
        GPIO.setup(Echo_EingangsPin, GPIO.IN)
        GPIO.output(Trigger_AusgangsPin, False)
        self.sleeptime= 1
        pass

    def read_value (self):
        writer= csv_123.csv_writer.CsvWriter()
        GPIO.setmode(GPIO.BCM) 
        Trigger_AusgangsPin = 17
        Echo_EingangsPin    = 27
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

                alarm=alerts.alert_service.AlertService()
                mindestAbstand= 2
                einheit="cm"
                alarm.set_alert_threshold(mindestAbstand,einheit)

                if Abstand < mindestAbstand or Abstand>300:
                    print("Abstand außerhalb des Messbereich")
                    print("------------------------------")
                    alarm.on_distance_threshold_passed(Abstand)
                else:
                    Abstand = format((Dauer * 34300) / 2, '.2f')
                    print("Der Abstand beträgt:", Abstand,("cm"))
                    print("------------------------------")
                    timestamp= datetime.datetime.now().isoformat();
                    #print(timestamp)
                    eintragJSON= {
                        "sensorId"  : "Ultraschall Sensor KY-050", 
                        "timestamp" : timestamp,
                        "distance"  : Abstand,
                        "unit"      : "cm"
                        }
                    writer.format_line(eintragJSON)
                time.sleep(self.sleeptime)

 
# Aufraeumarbeiten nachdem das Programm beendet wurde
        except KeyboardInterrupt:
            GPIO.cleanup()
    pass
