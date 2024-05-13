from secrets import token_urlsafe
from werkzeug.urls import url_fix
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("stand.html", error=request.args.get("error"))

@app.route("/new", methods=["POST"])
def create():
    content = request.form.get("content", "")
    return redirect(url_for("index", error=content))

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
