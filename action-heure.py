#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from datetime import datetime
from pytz import timezone

def verbalise_time(hours, minutes):
    spoken_time = ''

    if minutes in [35, 40, 45, 50, 55]:
        hours += 1

    if hours == 0:
        spoken_time += 'minuit'
    elif hours == 1:
        spoken_time += 'une heure'
    elif hours == 12:
        spoken_time += 'midi'
    elif hours == 21:
        spoken_time += 'vingt et une heures'
    else:
        spoken_time += '{0} heures'.format(str(hours))

    spoken_time += ' '

    if minutes == 0:
        spoken_time += ''
    elif minutes == 1:
        spoken_time += 'une'
    elif minutes == 21:
        spoken_time += 'vingt et une'
    elif minutes == 31:
        spoken_time += 'trente et une'
    elif minutes == 41:
        spoken_time += 'quarante et une'
    elif minutes == 51:
        spoken_time += 'cinquante et une'
    elif minutes == 15:
        spoken_time += 'et quart'
    elif minutes == 30:
        spoken_time += 'et demi'
    elif minutes == 35:
        spoken_time += 'moins vingt cinq'
    elif minutes == 40:
        spoken_time += 'moins vingt'
    elif minutes == 45:
        spoken_time += 'moins le quart'
    elif minutes == 50:
        spoken_time += 'moins dix'
    elif minutes == 50:
        spoken_time += 'moins cinq'
    else:
        spoken_time += '{0}'.format(str(minutes))

    return spoken_time

def subscribe_intent_callback(hermes, intent_message):
    now = datetime.now(timezone('Europe/Paris'))

    sentence = 'Il est '
    sentence += verbalise_time(now.hour, now.minute)

    hermes.publish_end_session(intent_message.session_id, sentence)

if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent('Joseph:askTime', subscribe_intent_callback).loop_forever()
