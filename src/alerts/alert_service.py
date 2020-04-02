class AlertService: # Service Reagiert auf Messwerte

    #  Initialisierung
    def __init__(self):
        pass

    #  value:  Neuer Schwellwert als einfache Zahl in der Einheit cm wird hier übergeben
    def set_alert_threshold (self, value, unit):
        self.mindestAbstand=value
        self.unit=unit

    #  value:  Aktuell gemessener Wert (siehe DistanceSensor) wird übergeben und es wird ein Alarm gesendet
    def on_distance_threshold_passed(self, value):
        print("Alarm, wir haben den Schwellwert von:", self.mindestAbstand, self.unit," unterschritten")
        pass