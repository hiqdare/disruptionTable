from flask import Flask
from flask import render_template
from . import app

@app.route("/")
def home():
    return render_template(
        "index.html",
        title='Table of Disruptive Technologies'
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")