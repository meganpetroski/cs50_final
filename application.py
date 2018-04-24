import os

from cs50 import SQL, eprint
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Ensure environment variable is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
# Ensure responses aren't cached
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///heartbeat.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # POST method
    if request.method == "POST":
        user = session["user_id"]
        # look up symbol input by user (choose from drop down list...)
        quote = lookup(request.form.get("symbol"))
        pdata = db.execute("SELECT * FROM portfolio")
        udata = db.execute("SELECT * FROM users")

        # resource https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_get_to_return_a_default_value_from_a_dictionary.html
        stock = ''
        if "symbol" in quote:
            stock = quote["symbol"]

        shares = ''
        if "shares" in pdata:
            shares = pdata["shares"]

        return render_template("index.html", stock=stock)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
    else:
        return render_template("index.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # POST method
    if request.method == "POST":
        # validate shares input
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("need valid number of shares", 400)
        # get stock, number of shares

        quote = lookup(request.form.get("symbol"))
        # check if symbol given is valid
        if not quote:
            return apology("Need valid symbol", 400)

        shares = int(request.form.get("shares"))

        # render apology if stock or share are blank
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("must provide valid stock symbol", 400)
        if int(request.form.get("shares")) < 0:
            return apology("need a positive number of shares!", 400)

        # define price again
        price = ''
        if "price" in quote:
            price = float(quote["price"])

        # time
        # resource https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-dates-and-times-legacy
        now = datetime.now()

        # calculate user
        user = session["user_id"]

        # calculate if user has enough cash
        cash = db.execute("SELECT cash FROM users WHERE id = :user", user=session["user_id"])
        for c in cash:
            money = float(c["cash"])
            # update cash as appropriate unless there's not enough, then apologize
            new_price = price * shares
            if money > new_price:
                new_money = round(money - new_price)
                # add stock to portfolio - keep track of stock symbol and number of shares
                # MISSING: should find if stock already exisits; if so update just the number of shares
                row = db.execute("INSERT INTO portfolio (id, stock, shares, price, timestamp) VALUES (:id, :stock, :shares, :price, :timestamp)",
                                 id=session["user_id"], stock=request.form.get("symbol"), shares=int(request.form.get("shares")), price=price, timestamp=now)
                # update users table with available cash
                row = db.execute("UPDATE users SET cash = :newmoney WHERE id = :user", newmoney=new_money, user=user)
                return render_template("index.html", price=price)
            else:
                return apology("not enough cash", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "POST":
        return render_template("history.html")
    else:
        return render_template("history.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # POST method
    if request.method == "POST":
        # look up symbol input by user
        quote = lookup(request.form.get("symbol"))

        # check if symbol given is valid
        if not quote:
            return apology("Need valid symbol", 400)

        # display symbol and price(in usd)
        # resource https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_get_to_return_a_default_value_from_a_dictionary.html
        stock = ''
        if "symbol" in quote:
            stock = quote["symbol"]

        price = ''
        if "price" in quote:
            price = usd(quote["price"])

        # only display the stock info if given a valid symbol
        return render_template("quoted.html", stock=stock, price=price)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    # GET method
    else:
        # show the quote template to the user
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # POST method
    if request.method == "POST":
        # get username, password, password confirmation from user via form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # render apology if username is blank or username already existst
        if not request.form.get("username"):
            return apology("must provide username", 400)
        # render apology if password is blank
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        # render apology if password and confirmation do not match
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("passwords must match", 400)

        else:
            # generate_password_hash()
            hash = generate_password_hash(request.form.get("password"))
            # add user name and hash for password to the db
            result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                                username=request.form.get("username"), hash=hash)
            if not result:
                return apology("This username is taken", 400)

            return redirect("/")

    # GET method
    else:
        # show the register template to the user
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # POST method
    if request.method == "POST":
        # get & validate stock, number of shares
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("need valid number of shares", 400)

        quote = lookup(request.form.get("symbol"))

        # check if symbol given is valid
        if not quote:
            return apology("Need valid symbol", 400)

         # peel apart elements
         # resource https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_get_to_return_a_default_value_from_a_dictionary.html
        stock = ''
        if "symbol" in quote:
            stock = quote["symbol"]

        price = ''
        if "price" in quote:
            price = usd(quote["price"])

        # get number of shares user wants to sell
        selling = request.form.get("shares")

        # apologize if user doesn't have any stock
        a = db.execute("SELECT * FROM portfolio WHERE id = :user AND stock = :stock", user=session["user_id"], stock=stock)
        if not a:
            return apology("you don't own any of this stock", 400)

        # apologize if wrong number of shares (not pos integer or don't own)
        b = db.execute("SELECT shares FROM portfolio WHERE id = :user AND stock = :stock", user=session["user_id"], stock=stock)
        number = ''
        if "shares" in quote:
            number = quote["shares"]
        if number < selling:
            return apology("you don't own enough of this stock", 400)

        # only display the stock info if given a valid symbol
        return render_template("sold.html", selling=selling, stock=stock, price=price, number=number)

        # update cash in users

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    # GET method
    else:
        # show the quote template to the user
        return render_template("sell.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
