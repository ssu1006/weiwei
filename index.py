from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>黃偲瑋 411134248 資管二B</h1>"
    homepage += "<a href=/about>偲瑋簡介網頁</a><br>"
    homepage += "<a href=/account>MIS相關工作簡介</a><br>"
    homepage += "<a href=/today>工作履歷</a><br>"
    return homepage



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/account", methods=["GET", "POST"])
def account():
        return render_template("account.html")

@app.route("/today")
def today():
    return render_template("today.html")

if __name__ == "__main__":
    app.run()