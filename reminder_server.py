#! usr/bin/env python

"""hacky project"""
import json

from flask import Flask, request
from flask_apscheduler import APScheduler

from reminder import add_reminder, display_time

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

scheduler.add_job(id='tick', func=display_time,
    trigger='interval', seconds=30)

@app.route("/", methods=['POST'])
def get_reminder():
    print(request.args)
    reminder_text = request.args['text']
    reminder_delay = int(request.args['delay'])
    add_reminder(scheduler, reminder_text, reminder_delay)
    return json.dumps({
        'status':'success',
        'text': reminder_text,
        'delay': reminder_delay
        })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
