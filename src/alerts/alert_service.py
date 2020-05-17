import mqtt.mqtt_Com as mqtt
class AlertService: # Service Reagiert auf Messwerte


    #  Initialisierung
    def __init__(self,pubsub):
        self.minimumdistance= 50
        self.unit = "cm"
        self.maximumdistance=300
        self.pubsub= pubsub
        pass

    #  value:  Neuer Schwellwert als einfache Zahl in der Einheit cm wird hier übergeben
    def set_alert_threshold (self, value, unit):
        self.minimumdistance=value
        self.unit=unit

    #  value:  Aktuell gemessener Wert (siehe DistanceSensor) wird übergeben und es wird ein Alarm gesendet
    def on_distance_threshold_passed(self, value):
        mqtt.mqttCommunication(self.pubsub).sendAlarm(value)
        if (float(value)>self.maximumdistance):
            print("Alarm, wir haben den Schwellwert von:", self.maximumdistance, self.unit,"mit", value, self.unit, " überschritten")

        else: 
            print("Alarm, wir haben den Schwellwert von:",self.minimumdistance , self.unit,"mit", value, self.unit, " unterschritten")
        pass

    