from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hey I am Alive." 

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

'''
This code, in summary, makes a website that just says "Hey I am Alive."

However, repl.it doesn't keep this code on 24/7. You need to make a GET request to this site every so often for it to run constantly.
This is where Uptime Robot comes in.

Go to https://uptimerobot.com and sign up with a free plan. Then create a monitor by clicking the button.

For monitor type, put Http(s). Put whatever unique name you want in Friendly Name. 
For URL (or IP) you want to put the URL that the flask shows up on. Once you run the discord bot on repl,
a box appears on the top-right of the interface with the URL.

That's it! It's done. Just click run on repl.it and you can close the tab. It works!
'''