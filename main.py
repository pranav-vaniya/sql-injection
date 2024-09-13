# the code in this project has been intentionally written in a bad fashion to showcase sql injection and what-not-to-do

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "the_secure_banks_super_secret_key"  # will be used for session cookies, not really a worry for us

CURR_DIR = Path(__file__).parent
dbpath = CURR_DIR / "database" / "users.db"


@app.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    return render_template("index.html")


@app.route("/login")
def login():
    if session.get("logged_in"):
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/login-user", methods=["POST"])
def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    isValidUser = False

    userdb_conn = sqlite3.connect(dbpath)
    userdb_cursor = userdb_conn.cursor()
    data = userdb_cursor.execute(
        f"SELECT * FROM USERS WHERE username='{username}' and password='{password}'"
    )

    if len(data.fetchall()) == 1:
        isValidUser = True

    if isValidUser:
        session["logged_in"] = True
        return jsonify({"message": "Login successful"}), 200

    else:
        return jsonify({"message": "Invalid username or password"}), 401


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
