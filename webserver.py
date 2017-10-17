"""
webserver.py
File that is the central location of code for your webserver.
"""
import os
from flask import Flask, redirect, render_template, request, abort
from os import environ
import json
import requests


app = Flask(__name__,static_url_path="/static")

@app.route('/index')
def index():
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/about')
def about():
    return render_template("aboutus.html")

@app.route('/blog/<fname>')
def blog(fname):
    return render_template(fname + '.html')


@app.route('/contact',methods=['GET'])
def contact():
  print
  return render_template("contactus.html")

USER  = environ['INFO253_MAILGUN_USER'] 
PASS  = environ['INFO253_MAILGUN_PASSWORD'] 
FROM = environ['INFO253_MAILGUN_FROM_EMAIL']
TO   = environ['INFO253_MAILGUN_TO_EMAIL']
DOMAIN   = environ['INFO253_MAILGUN_DOMAIN'] 

@app.route('/f', methods=['POST'])
def form():
  print(USER)
  print(PASS)
  print(FROM)
  data = json.loads(request.data.decode('ascii'))
  r=requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(DOMAIN),
        auth=(USER, PASS),
        data={"from": data['name'] + " " + FROM,
              "to": TO,
              "subject": data['subject'],
              "text": data['msg'] +
                     '\n You have received mail from ' + data['name'] })
  print(r.text)
  return ('', 204)
