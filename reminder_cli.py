#!/usr/bin/env python

"""
CLI interface to send reminders to the raspberry pi
"""

import requests

SERVER_URL = 'http://192.168.1.155:5000'

def post_reminder(reminder_text, reminder_delay):
    print('Adding a reminder with text:\n{} and delay: {}'.format(reminder_text,
        reminder_delay))
    result = requests.post(SERVER_URL, params={'text': reminder_text, 'delay': reminder_delay})
    if result.ok:
        print('Reminder added succesfully')
    else:
        print('There was an error with your request.\n{}'.format(result.content))

if __name__=='__main__':
    import sys
    reminder_text = ' '.join(sys.argv[1:-1])
    reminder_delay = int(sys.argv[-1])
    post_reminder(reminder_text, reminder_delay)
