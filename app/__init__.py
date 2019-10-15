from flask import Flask, jsonify
from functools import reduce
from .api.desk_allocation import expose_api
from .api.scripts.timetable import make_table
import csv
import os

app = Flask(__name__,
            static_url_path='',
            static_folder="../dist",
            template_folder="../dist")


@app.route('/api/getSchedule')
def say_hello():
    return jsonify(make_table())


@app.route("/")
def index():
    return app.send_static_file("index.html")
