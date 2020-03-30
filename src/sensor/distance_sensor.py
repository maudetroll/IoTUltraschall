import time
import RPi.GPIO as GPIO
import datetime
import csv_123.csv_writer

class DistanceSensor:
    var=5
    def __init__(self):
        GPIO.setmode(GPIO.BCM) 
        Trigger_AusgangsPin = 17
        Echo_EingangsPin    = 27
        GPIO.setup(Trigger_AusgangsPin, GPIO.OUT)
        GPIO.setup(Echo_EingangsPin, GPIO.IN)
        GPIO.output(Trigger_AusgangsPin, False)
        sleeptime= 0.8
        pass

    #  return Wert als Dictionary entsprechend folgendem JSON:
    #   { 
    #     "sensorId"  : "KY-050", 
    #     "timestamp" : "2020-03-01T12:00:01.345+01:00",
    #     "distance" : 42,
    #     "unit" : "cm"
    #   }
    def read_value (self):
        writer= csv_123.csv_writer.CsvWriter()
        GPIO.setmode(GPIO.BCM) 
        Trigger_AusgangsPin = 17
        Echo_EingangsPin    = 27
        GPIO.setup(Trigger_AusgangsPin, GPIO.OUT)
        GPIO.setup(Echo_EingangsPin, GPIO.IN)
        GPIO.output(Trigger_AusgangsPin, False)
        sleeptime= 0.8
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

                if Abstand < 2 or (round(Abstand) > 300):
                    # Falls nicht wird eine Fehlermeldung ausgegeben
                    print("Abstand außerhalb des Messbereich")
                    print("------------------------------")
                else:
                    Abstand = format((Dauer * 34300) / 2, '.2f')
                    print("Der Abstand beträgt:", Abstand,("cm"))
                    print("------------------------------")
                    timestamp= datetime.datetime.now().isoformat();
                    print(timestamp)
                    eintragJSON= {
                        "sensorId"  : "Ultraschall Sensor KY-050", 
                        "timestamp" : timestamp,
                        "distance"  : Abstand,
                        "unit"      : "cm"
                        }
                    writer.format_line(eintragJSON)
                    print(eintragJSON)
                    # Pause zwischen den einzelnen Messungen
                time.sleep(sleeptime)

 
# Aufraeumarbeiten nachdem das Programm beendet wurde
        except KeyboardInterrupt:
            GPIO.cleanup()

    
    pass
