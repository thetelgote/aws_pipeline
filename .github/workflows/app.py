from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to My Flask App!"

@app.route("/api/echo", methods=["GET"])
def echo():
    message = request.args.get("msg", "")
    return jsonify({"response": f"You said: {message}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
