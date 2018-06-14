#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


verbalisation = {
	"0": "minuit",
	"1": "une heure",
	"2": "deux heures",
	"3": "trois heures",
	"4": "quatre heures",
	"5": "cinq heures",
	"6": "six heures",
	"7": "sept heures",
	"8": "huit heures",
	"9": "neuf heures",
	"10": "dix heures",
	"11": "onze heures",
	"12": "midi",
	"13": "treize heures",
	"14": "quatorze heures",
	"15": "quinze heures",
	"16": "seize heures",
	"17": "dix-sept heures",
	"18": "dix-huit heures",
	"19": "dix-neuf heures",
	"20": "ving heures",
	"21": "ving-et-une heures",
	"22": "vingt deux heures",
	"23": "vingt troi heures"
}

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
