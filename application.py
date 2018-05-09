import re
import cs50
from html import escape
from werkzeug.exceptions import default_exceptions, HTTPException
from helpers import lines

import os
import csv
import requests

from contextlib import closing
from html import escape
from flask import Flask, render_template, request, make_response, send_file, abort, redirect

from cs50 import SQL

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///heartbeat.db")

@app.route("/")
def home():

    return render_template("home.html")

@app.route("/about_us")
def about_us():

    return render_template("about_us.html")

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
    download = db.execute("SELECT buildnumber, product, region, attribution, query, result_text, result_count FROM data WHERE buildnumber = :buildnumber", buildnumber=buildnum_ret)
    htmlcsv = db.execute("SELECT * FROM data WHERE buildnumber = :buildnumber", buildnumber=buildnum_ret)

    # dynamically attach build number to csv output
    csvfile = ("{}.csv".format(buildnum_ret))

    # write results to csv
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for row in download:
            writer.writerow([row])

    return render_template("result.html", runs=runs, htmlcsv=htmlcsv)

@app.route("/compare_home")
def compare_home():

    return render_template("compare_home.html")

@app.route("/compare", methods=["POST"])
def compare():
    # resource: pset6 similiarities less version
    # Read files
    if not request.files["file1"] or not request.files["file2"]:
        abort(400, "missing file")
    try:
        file1 = request.files["file1"].read().decode("utf-8")
        file2 = request.files["file2"].read().decode("utf-8")
    except Exception:
        abort(400, "invalid file")

    # Compare files
    if not request.form.get("algorithm"):
        abort(400, "missing algorithm")
    elif request.form.get("algorithm") == "lines":
        matches = lines(file1, file2)
    else:
        abort(400, "invalid algorithm")

    # Output comparison
    return render_template("compare.html", file1=file1, file2=file2)

@app.errorhandler(HTTPException)
def errorhandler(error):
    """Handle errors"""
    # resource: pset6 similiarities less version
    return render_template("error.html", error=error), error.code

# resource: pset6 similiarities less version
# https://github.com/pallets/flask/pull/2314
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


