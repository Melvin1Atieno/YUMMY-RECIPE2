from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user_registration")
def registration():
    return render_template("USER_REGISTRATION.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
         if request.form["username"] == " " or request.form["password"] == " ":
            error = "fields cannot be empty"
        else:
            return redirect(url_for("homepage"))
    return render_template("LOGIN.html", error=error)

@app.route("/logout")
def logout():
    return redirect(url_for("login"))


@app.route("/homepage")
def homepage():
    return render_template("HOMEPAGE.html")


if __name__ == "__main__":
    debug = True
    app.run()
