import os
import calendar

from flask import Flask, render_template, request

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

    return render_template("home.html")
    # return "The website, it works!!"

@app.route("/compare")
def compare():

    return render_template("compare.html")

@app.route("/query")
def query():

    return render_template("query.html")

