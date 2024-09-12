from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "the_secure_banks_super_secret_key"  # will be used for session cookies, not really a worry for us


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

    if username == "user" and password == "pass":
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
