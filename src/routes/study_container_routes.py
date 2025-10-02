from flask import jsonify, render_template, request, redirect, url_for
from src.data.db_context import app
from src.middleware.auth_middleware import login_required 

@app.route('/admin/containers')
@login_required
def containers():
    return render_template('study_container/index.html')