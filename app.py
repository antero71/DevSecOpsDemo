from flask import Flask, request, render_template

app = Flask(__name__)

@app.after_request
def set_security_headers(resp):
    resp.headers['X-Frame-Options'] = 'DENY'
    resp.headers['X-Content-Type-Options'] = 'nosniff'
    resp.headers['Content-Security-Policy'] = "default-src 'self'; object-src 'none'; base-uri 'self';"
    resp.headers['Permissions-Policy'] = 'geolocation=(), camera=(), microphone=()'
    resp.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = '0'
    return resp

@app.route("/")
def home():
    return "Hello from DevSecOps Demo!"

@app.route("/echo", methods=["GET", "POST"])
def echo():
    data = request.args.get("input") or request.form.get("input")
    return render_template("echo.html", data=data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)