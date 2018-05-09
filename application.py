import re
import cs50
from html import escape
from werkzeug.exceptions import default_exceptions, HTTPException
from helpers import lines

import os
import calendar
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

    # Highlight files
    highlights1 = highlight(file1, matches)
    highlights2 = highlight(file2, matches)

    # Output comparison
    return render_template("compare.html", file1=highlights1, file2=highlights2)

def highlight(s, strings):
    """Highlight all instances of strings in s."""

    # Get intervals for which strings match
    intervals = []
    for string in strings:
        if not string:
            continue
        matches = [match.start() for match in re.finditer(re.escape(string), s)]
        for match in matches:
            intervals.append((match, match + len(string)))
    intervals.sort(key=lambda x: x[0])

    # Combine intervals to get highlighted areas
    highlights = []
    for interval in intervals:
        if not highlights:
            highlights.append(interval)
            continue
        last = highlights[-1]

        # If intervals overlap, then merge them
        if interval[0] <= last[1]:
            new_interval = (last[0], interval[1])
            highlights[-1] = new_interval

        # Else, start a new highlight
        else:
            highlights.append(interval)

    # Maintain list of regions: each is a start index, end index, highlight
    regions = []

    # If no highlights at all, then keep nothing highlighted
    if not highlights:
        regions = [(0, len(s), False)]

    # If first region is not highlighted, designate it as such
    elif highlights[0][0] != 0:
        regions = [(0, highlights[0][0], False)]

    # Loop through all highlights and add regions
    for start, end in highlights:
        if start != 0:
            prev_end = regions[-1][1]
            if start != prev_end:
                regions.append((prev_end, start, False))
        regions.append((start, end, True))

    # Add final unhighlighted region if necessary
    if regions[-1][1] != len(s):
        regions.append((regions[-1][1], len(s), False))

    # Combine regions into final result
    result = ""
    for start, end, highlighted in regions:
        escaped = escape(s[start:end])
        if highlighted:
            result += f"<span>{escaped}</span>"
        else:
            result += escaped
    return result


@app.errorhandler(HTTPException)
def errorhandler(error):
    """Handle errors"""
    return render_template("error.html", error=error), error.code


# https://github.com/pallets/flask/pull/2314
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


