from flask import Flask, render_template, url_for, request, redirect, session
from YUMMY.models import UserAccount


app = Flask(__name__)
# session = session()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user_registration", methods=["GET","POST"])
def registration():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        new_user = UserAccount()
        new_user.add_new(email, username, password, confirm_password)
        return redirect(url_for("login"))
    else:
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



if __name__ == "__main__":
    app.secret_key = "0456155"
    app.config["SESSION_TYPE"] = "filesystem"

    app.run(debug=True)
