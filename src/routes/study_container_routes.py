from flask import render_template, request, redirect, url_for, session
from src.data.db_context import app
from src.middleware.auth_middleware import login_required 
from src.services.study_container_service import StudyContainerService

study_container_service = StudyContainerService()
@app.route('/admin/containers')
@login_required
def containers():
    user_id = session.get('user_id')
    containers = study_container_service.get_all_containers(user_id)
    return render_template('study_container/index.html', containers=containers)

@app.route('/admin/containers', methods=['POST'])
@login_required
def containers_post():
    name = request.form.get('cardName')
    description = request.form.get('cardDescription')
    user_id = session.get('user_id')
    if name and description:
        study_container_service.create_container(name, description, user_id)
    return redirect(url_for('containers'))