from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevSecOps Demo!"

@app.route("/echo", methods=["GET", "POST"])
def echo():
    data = request.args.get("input") or request.form.get("input")
    return f"You sent: {data}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)