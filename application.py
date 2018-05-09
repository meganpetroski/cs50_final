import os
import calendar
import csv
import requests

from contextlib import closing
from html import escape
from flask import Flask, render_template, request, make_response, send_file
from helpers import lines, sentences, substrings

from cs50 import SQL

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///heartbeat.db")

@app.route("/")
def index():

    return render_template("home.html")

@app.route("/compare")
def compare():

    return render_template("compare.html")

@app.route("/query")
def query():

    return render_template("query.html")

@app.route("/result")
def result():
    # get a list of run numbers
    runs = db.execute("SELECT DISTINCT buildnumber FROM data")

    # return the build number chosen by the drop down menu
    buildnum_ret = request.args.get('runs')

    # data to download
    download = db.execute("SELECT * FROM data WHERE buildnumber = :buildnumber", buildnumber=buildnum_ret)

    # dynamically attach build number to csv output
    csvfile = ("{}.csv".format(buildnum_ret))

    # write results to csv
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for row in download:
            writer.writerow([row])

    return render_template("result.html", runs=runs, download=download)


