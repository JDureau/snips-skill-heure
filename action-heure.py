#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from datetime import datetime
from pytz import timezone



def verbalise_hour(i):
    if i == 0:
        return "minuit"
    elif i == 1:
        return "une heure"
    elif i == 12:
        return "midi"
    elif i == 21:
        return "vingt et une heures"
    else:
        return "{0} heures".format(str(i))

def verbalise_minute(i):
    if i == 0:
        return ""
    elif i == 1:
        return "une"
    elif i == 21:
        return "vingt et une"
    elif i == 31:
        return "trente et une"
    elif i == 41:
        return "quarante et une"
    elif i == 51:
        return "cinquante et une"
    else:
        return "{0}".format(str(i))


def subscribe_intent_callback(hermes, intent_message):
    print()
    print(intent_message.intent.intent_name)
    print()

    if intent_message.intent.intent_name == 'Joseph:askTime':

        sentence = 'Il est '
        print(intent_message.intent.intent_name)

        now = datetime.now(timezone('Europe/Paris'))

        sentence += verbalise_hour(now.hour) + " " + verbalise_minute(now.minute)
        print(sentence)

        # hermes.publish_continue_session(intent_message.session_id, sentence, ["Joseph:greetings"])
        hermes.publish_end_session(intent_message.session_id, sentence)

    elif intent_message.intent.intent_name == 'Joseph:greetings':

        hermes.publish_end_session(intent_message.session_id, "De rien!")


if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent('Joseph:askTime', subscribe_intent_callback).loop_forever()
