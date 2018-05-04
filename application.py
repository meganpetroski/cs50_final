import os
import calendar

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
    # sample a record from heartbeat.db
    sample = db.execute("SELECT * FROM results")

    # cal = (calendar.calendar(2018))
    # print(cal)

    return render_template("home.html", sample=sample)

@app.route("/compare")
def compare():
    # get a list of run numbers
    dates1 = db.execute("SELECT DISTINCT buildnumber FROM data")

    return render_template("compare.html", dates1=dates1)

@app.route("/compared")
def compared():
    # get the data from run #1
    file1 = db.execute("SELECT * FROM data WHERE buildnumber = :file1", file1='11723')

    # get the data from run #2
    file2 = db.execute("SELECT * FROM data WHERE buildnumber = :file2", file2='11607')

    return render_template("compared.html", file1=file1)


    # read files
    # if not request.files["file1"] or not request.files["file2"]:
    #     abort(400, "missing file")
    # try:
    #     file1 = request.files["file1"].read().decode("utf-8")
    #     file2 = request.files["file2"].read().decode("utf-8")
    # except Exception:
    #     abort(400, "invalid file")

    # # Compare files
    # if not request.form.get("algorithm"):
    #     abort(400, "missing algorithm")
    # elif request.form.get("algorithm") == "lines":
    #     matches = lines(file1, file2)
    # elif request.form.get("algorithm") == "sentences":
    #     matches = sentences(file1, file2)
    # elif request.form.get("algorithm") == "substrings":
    #     if not request.form.get("length"):
    #         abort(400, "missing length")
    #     elif not int(request.form.get("length")) > 0:
    #         abort(400, "invalid length")
    #     matches = substrings(file1, file2, int(request.form.get("length")))
    # else:
    #     abort(400, "invalid algorithm")

    # # Highlight files
    # highlights1 = highlight(file1, matches)
    # highlights2 = highlight(file2, matches)

    # Output comparison

    # , file1=highlights1, file2=highlights2)



# def highlight(s, strings):
#     """Highlight all instances of strings in s."""

#     # Get intervals for which strings match
#     intervals = []
#     for string in strings:
#         if not string:
#             continue
#         matches = [match.start() for match in re.finditer(re.escape(string), s)]
#         for match in matches:
#             intervals.append((match, match + len(string)))
#     intervals.sort(key=lambda x: x[0])

#     # Combine intervals to get highlighted areas
#     highlights = []
#     for interval in intervals:
#         if not highlights:
#             highlights.append(interval)
#             continue
#         last = highlights[-1]

#         # If intervals overlap, then merge them
#         if interval[0] <= last[1]:
#             new_interval = (last[0], interval[1])
#             highlights[-1] = new_interval

#         # Else, start a new highlight
#         else:
#             highlights.append(interval)

#     # Maintain list of regions: each is a start index, end index, highlight
#     regions = []

#     # If no highlights at all, then keep nothing highlighted
#     if not highlights:
#         regions = [(0, len(s), False)]

#     # If first region is not highlighted, designate it as such
#     elif highlights[0][0] != 0:
#         regions = [(0, highlights[0][0], False)]

#     # Loop through all highlights and add regions
#     for start, end in highlights:
#         if start != 0:
#             prev_end = regions[-1][1]
#             if start != prev_end:
#                 regions.append((prev_end, start, False))
#         regions.append((start, end, True))

#     # Add final unhighlighted region if necessary
#     if regions[-1][1] != len(s):
#         regions.append((regions[-1][1], len(s), False))

#     # Combine regions into final result
#     result = ""
#     for start, end, highlighted in regions:
#         escaped = escape(s[start:end])
#         if highlighted:
#             result += f"<span>{escaped}</span>"
#         else:
#             result += escaped
#     return result
#     return render_template("compare.html", dates1=dates1)

@app.route("/query")
def query():

    return render_template("query.html")

@app.route("/result")
def result():

    return render_template("result.html")
