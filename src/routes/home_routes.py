from flask import jsonify, render_template, request, redirect, url_for
from main import app


@app.route('/')
def index():
    return render_template('index.html')