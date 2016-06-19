# Raspberry Reminder

If you have the following:

1. A raspberry pi, connected to your wifi network. I also have the [sense hat]https://www.raspberrypi.org/products/sense-hat/) module. If you dont have it you can remove the `sense` related code.
2. A speaker connected to the Raspberry
3. Python

Then you can use this to set loud reminders with a delay from your main computer.

In my case I use it to remind me to go to bed before a certain time.

This is a very rough, done in less than 3 hours implementation. Works for me, and it should be easy to adapt it to your needs

# How to run

1. Copy/Clone repository on the raspberry pi
2. Install requirements on requirements.txt on the raspberry pi.
3. Run the flask app `reminder_server.py` on your server (you will need to use something like `screen` so it doesnt stop when you leave the remote session).
4. Edit your `.bash_aliases` and add an alias to the cli interface `reminder_cli.py` like:

```
# alias for raspberry pi reminder
alias remind='/path/to/reminder_cli.py'
```

The file `reminder_cli.py` needs to be somewhere on your main computer

So, when I want to give me only one hour (and only one, not 5 or 8) of browsing reddit before going to bed,  I can do something like:

`remind go to sleep 3600`

Will send an http request to the flask app on the raspberry, and set up an scheduled job with a delay of 3600 seconds (1 hour).

Then, after that delay, the task will run, will connect to Google Text-To-Speech Speech API (using the awesome [gTTS](https://github.com/pndurette/gTTS) wrapper), create and mp3, and play it on the Raspberry's speakers.
