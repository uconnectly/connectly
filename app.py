from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # TEMP logic (Phase 1)
    if email and password:
        return f"✅ Logged in as {email}"
    else:
        return "❌ Missing email or password", 400

@app.route("/signup", methods=["POST"])
def signup():
    email = request.form.get("email")
    password = request.form.get("password")

    # TEMP logic (Phase 1)
    if email and password:
        return f"🎉 Account created for {email}"
    else:
        return "❌ Missing email or password", 400


if __name__ == "__main__":
    app.run(debug=True)
