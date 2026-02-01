from flask import Flask, render_template, request
from model import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    msg = request.args.get("msg")
    reply = get_response(msg)
    return reply

if __name__ == "__main__":
    app.run(debug=True)
