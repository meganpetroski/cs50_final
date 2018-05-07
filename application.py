import os
import calendar
import csv
import requests

from contextlib import closing
from html import escape
from flask import Flask, render_template, request
from helpers import lines, sentences, substrings

from cs50 import SQL

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///heartbeat.db")

@app.route("/")
def index():

    return render_template("home.html")

@app.route("/download")
def download():
    # get a list of run numbers
    runs = db.execute("SELECT DISTINCT buildnumber FROM data")

    buildnum_ret = request.args.get('buildnumber')
    print(buildnum_ret)

    download1 = db.execute("SELECT * FROM data WHERE buildnumber = :buildnumber", buildnumber='11723')

    csvfile = ("{}.csv".format(11723))

    #Assuming res is a flat list
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for row in download1:
            writer.writerow([row])

    return render_template("download.html", runs=runs, download1=download1)

@app.route("/compare")
def compare():
    # get the data from run #1
    file1 = db.execute("SELECT * FROM data WHERE buildnumber = :file1", file1='11723')

    # get the data from run #2
    file2 = db.execute("SELECT * FROM data WHERE buildnumber = :file2", file2='11607')

    return render_template("compare.html", file1=file1)

@app.route("/query")
def query():

    return render_template("query.html")

@app.route("/result")
def result():
    # get a list of run numbers
    dates1 = db.execute("SELECT DISTINCT buildnumber FROM data")

    return render_template("result.html", dates1=dates1)

@app.route("/results")
def results():
    # get the data from the run number selected
    file1 = db.execute("SELECT * FROM data WHERE buildnumber = :file1", file1='11723')

    #if_name_=="_main_":
        #app.run()

    return render_template("results.html", file1=file1)


    ##return render_template("result.html")
