from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevSecOps Demo!"

@app.route("/echo", methods=["GET", "POST"])
def echo():
    data = request.args.get("input") or request.form.get("input")
    return render_template_string("You sent: {{ data }}", data=data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)