#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):
    sentence = 'Il est '

    if intent_message.intent.intent_name == 'Joseph:askTime':
        print(intent_message.intent.intent_name)

    now = datetime.now()

    sentence += str(now.hour) + " heures " + str(now.minute)
    print(sentence)

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
