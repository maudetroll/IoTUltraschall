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
        print("Es muss ein neuer Mindestabstand eingehalten werden: ",AlertService.minimumdistance)
        self.unit=unit

        self.on_distance_threshold_passed(100);

    #  value:  Aktuell gemessener Wert (siehe DistanceSensor) wird übergeben und es wird ein Alarm gesendet
    def on_distance_threshold_passed(self, value):
        mqtt.mqttCommunication(self.pubsub).sendAlarm(value)
        print(AlertService.minimumdistance)

        if (float(value)>AlertService.maximumdistance):
            print("Alarm, wir haben den Schwellwert von:", AlertService.maximumdistance, self.unit,"mit", value, self.unit, " überschritten")

        else: 
            print("Alarm, wir haben den Schwellwert von:",AlertService.minimumdistance , self.unit,"mit", value, self.unit, " unterschritten")
        pass

    