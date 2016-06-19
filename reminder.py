#! usr/bin/env python

import os
from datetime import datetime, timedelta
import random
import uuid
import pytz

from gtts import gTTS
from sense_hat import SenseHat


sense = SenseHat()
sense.show_message("Starting", scroll_speed=0.01)
spain_timezone = pytz.timezone('Europe/Madrid')

def display_time():
    text_color = [random.randint(0, 255)for i in range(3)]
    tick = datetime.now(spain_timezone)
    sense.show_message(datetime.strftime(tick, '%H:%M'), text_colour=text_color, scroll_speed=0.01)

def create_reminder_audio(reminder_text, lang='en'):
    tts = gTTS(text=reminder_text, lang=lang)
    tts.save('reminder.mp3')

def play_reminder_audio():
    print('playing')
    os.system('omxplayer reminder.mp3')

def remind(reminder_text):
    create_reminder_audio(reminder_text)
    play_reminder_audio()

def add_reminder(scheduler, reminder_text, reminder_delay):
    scheduled_time = datetime.utcnow() + timedelta(seconds=reminder_delay)
    job_id = str(uuid.uuid4())
    scheduler.add_job(id=job_id, func=remind, trigger='date',
        run_date=scheduled_time,
            args=[reminder_text]
        )
    sense.show_message('OK!', text_colour=[0, 252, 0], scroll_speed=0.01)
