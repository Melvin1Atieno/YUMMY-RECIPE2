from yummy import app

if __name__ == "__main__":
    app.secret_key = "0456155"
    app.config["SESSION_TYPE"] = "filesystem"

    app.run(debug=True)
