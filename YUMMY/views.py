from flask import Flask, render_template, url_for, request, redirect, session, flash, Markup
from .models import UserAccount
# from .forms import UserRegistrationForm, LoginForm

from YUMMY import app

# Set variable to check if user is logged in
loggedIn = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user_registration", methods=["GET","POST"])
def registration():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        new_user = UserAccount()
        if loggedIn:
            user_already_logged_in = Markup("<div class='alert alert-info' role='alert'>\
                                                             The user is already logged in\
                                                  </div>")
            flash(user_already_logged_in)
            return redirect(url_for("registration"))
        else:
            results = new_user.add_new(email, username, password)
            if results == "exists":
                email_exists = Markup("<div class='alert alert-info' role='alert'>\
                                                       The email you entered is registered to another user\
                                          </div>")
                flash(email_exists)
                return redirect(url_for("registration"))
            registered = Markup("<div class='alert alert-info' role='alert'>\
                                                       you have been successfullly registered\
                                          </div>")
            flash(registered)
            return redirect(url_for("login"))
    else:
        # form = UserRegistrationForm(request.form())
        return render_template("USER_REGISTRATION.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        new_user = UserAccount()
        new_user.confirm(username, password)
        # username = session["username"] #save "username" in session
        return redirect(url_for("homepage"))
    return render_template("LOGIN.html")

@app.route("/homepage", methods=["POST","GET"])
def homepage():
    return render_template("HOMEPAGE.html")

@app.route("/logout")
def logout():
    #removes "username" from the session if it exists
    # session.pop("usename", None)
    return redirect(url_for("login"))
