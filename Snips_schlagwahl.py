#!/usr/bin/env python3

import paho.mqtt.client as mqtt 
from hermes_python.hermes import Hermes, MqttOptions
import os

USERNAME_INTENTS = "xopsa"
MQTT_BROKER_ADDRESS = "localhost:1883"
MQTT_USERNAME = None
MQTT_PASSWORD = None

	
def user_intent(intentname):
    return USERNAME_INTENTS + ":" + intentname


def schlagAuswahl(hermes, intent_message):
    intentname = intent_message.intent.intent_name
    schlag = intentMessage.slots.schlag.first().value
    result_sentence = "Die Auswahl ist: {}".format(str(schlag)
    #print("Schlag ausm GitHub ausgeführt: {}!!!".format(str(schlag)))
    current_session = intent_message.session_id
    hermes.publish_end_session(current_session, result_sentence)


def farbAuswahl(hermes, intent_message):
    intentname = intent_message.intent.intent_name
    farbe = intentMessage.slots.farbe.first().value
    result_sentence = "Die Auswahl ist: {}".format(str(farbe))
    #print("Farbe ausm GitHub ausgeführt: {}!!!".format(str(farbe)))
    current_session = intent_message.session_id
    hermes.publish_end_session(current_session, result_sentence)

if __name__ == "__main__":
    snips_config = toml.load('/etc/snips.toml')
    if 'mqtt' in snips_config['snips-common'].keys():
        MQTT_BROKER_ADDRESS = snips_config['snips-common']['mqtt']
    if 'mqtt_username' in snips_config['snips-common'].keys():
        MQTT_USERNAME = snips_config['snips-common']['mqtt_username']
    if 'mqtt_password' in snips_config['snips-common'].keys():
        MQTT_PASSWORD = snips_config['snips-common']['mqtt_password']

    mqtt_opts = MqttOptions(username=MQTT_USERNAME, password=MQTT_PASSWORD, broker_address=MQTT_BROKER_ADDRESS)
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intents(schlagAuswahl)
	h.subscribe_intents(farbAuswahl)
	h.start()
