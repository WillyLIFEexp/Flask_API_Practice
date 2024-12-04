
import json
import re

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>This is the main page!</p>"

@app.route("/greed/", defaults={ 'name': 'World' }, methods = ['GET'])
@app.route('/greed/<name>')
def show_user_profile(name):
    return json.dumps({'message': f"Hello, {escape(name)}!"})

@app.errorhandler(404)
def page_not_found(e):
    error_link = re.findall(r'.*?:\/\/.*?\/(.*)', request.url)
    if len(error_link) > 0:
        err_para = error_link[-1]
    else:
        err_para = "unknown"
    return f"Currently url path: /{escape(err_para)} is not working. Please check /greed or /"
