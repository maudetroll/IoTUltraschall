import os
import json

class Configuration:

    config ={
        "broker_host": None,
        "broker_port": None,
        "config_topic": None,
        "data_topic": None,
        "alert_topic": None
    }

    def __init__(self,configpath='brokerConfig.json'):
        pathConfig= os.path.join(os.path.dirname(__file__), configpath)

        with open(pathConfig) as file:
            config= json.load(file)
        
        Configuration.config["broker_host"] = config["broker_host"]
        Configuration.config["broker_port"] = config["broker_port"]
        Configuration.config["config_topic"] = config["config_topic"]
        Configuration.config["data_topic"] = config["data_topic"]
        Configuration.config["alert_topic"] = config["alert_topic"]
