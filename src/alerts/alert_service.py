import mqtt.mqtt_Com as mqtt
class AlertService: # Service Reagiert auf Messwerte

    minimumdistance= 50
    maximumdistance=300
    #  Initialisierung
    def __init__(self,pubsub):
        self.minimumdistance= AlertService.minimumdistance
        self.unit = "cm"
        self.maximumdistance=AlertService.maximumdistance
        self.pubsub= pubsub
        pass

    #  value:  Neuer Schwellwert als einfache Zahl in der Einheit cm wird hier übergeben
    def set_alert_threshold (self, value, unit):
        AlertService.minimumdistance= int(value)
        self.unit=unit

    #  value:  Aktuell gemessener Wert (siehe DistanceSensor) wird übergeben und es wird ein Alarm gesendet
    def on_distance_threshold_passed(self, value):
        if (float(value)>AlertService.maximumdistance):
            print("Alarm, wir haben den Schwellwert von:", AlertService.maximumdistance, self.unit,"mit", value, self.unit, " überschritten")
            mqtt.mqttCommunication(self.pubsub).sendAlarm_tohigh(value)
        elif (float(value)<AlertService.minimumdistance): 
            print("Alarm, wir haben den Schwellwert von:",AlertService.minimumdistance , self.unit,"mit", value, self.unit, " unterschritten")
            mqtt.mqttCommunication(self.pubsub).sendAlarm(value)
        pass

    