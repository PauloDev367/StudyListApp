from flask import jsonify, render_template, request, redirect, url_for
from src.data.db_context import app

@app.route('/containers')
def containers():
    return render_template('study_container/index.html')