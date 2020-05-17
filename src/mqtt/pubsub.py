import os, threading
import time
class Pubsub:
 
    def __init__(self):
        self._topics = {}

    def publish(self, topic, *args, **kwargs):
        if topic in self._topics:
            for methode in self._topics[topic]:
                thread=threading.Thread(target=methode, name=(str("iot-"+topic)+" "+str(methode)), \
                        args=args, kwargs=kwargs)
                thread.start() 
                time.sleep(10)


    def subscribe(self, topic, funktion):
        if not topic in self._topics:
            self._topics[topic] = []
        self._topics[topic].append(funktion)

    def unsubcribe(self, topic, funktion):
        if not topic in self._topics:
            return
        self._topics[topic].remove(funktion)


