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

@app.route('/admin/containers/<int:container_id>/delete', methods=['POST'])
@login_required
def delete_container(container_id):
    user_id = session.get('user_id')
    study_container_service.delete_container(container_id, user_id)
    return redirect(url_for('containers'))

@app.route('/admin/containers/<int:container_id>/edit', methods=['POST'])
@login_required
def edit_container(container_id):
    name = request.form.get('editCardName')
    description = request.form.get('editCardDescription')
    user_id = session.get('user_id')
    if name and description:
        study_container_service.update_container(container_id, name, description, user_id)
    return redirect(url_for('containers'))