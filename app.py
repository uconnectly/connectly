from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return "🚀 Connectly is live!"

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    users.append({
        "username": data.get("username"),
        "niche": data.get("niche"),
        "posts": 0,
        "badge": "New Creator"
    })
    return jsonify({"message": "User created successfully"})

@app.route("/post", methods=["POST"])
def create_post():
    username = request.json.get("username")
    for user in users:
        if user["username"] == username:
            user["posts"] += 1
            if user["posts"] >= 3:
                user["badge"] = "🔥 Active Creator"
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run()
