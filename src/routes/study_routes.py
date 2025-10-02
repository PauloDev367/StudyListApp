from flask import render_template, request, redirect, url_for, session
from src.data.db_context import app
from src.middleware.auth_middleware import login_required 
from src.services.study_service import StudyService

study_service = StudyService()
@app.route('/admin/container/<int:container_id>/cards', methods=['POST'])
@login_required
def add_study_to_container(container_id):
    name = request.form.get('name')
    description = request.form.get('description')
    user_id = session.get('user_id')
    link = request.form.get('link')
    study_service.create_study(name, description, link, container_id, user_id)
    return redirect(url_for('view_container_cards', container_id=container_id))

@app.route('/admin/container/<int:container_id>/cards/<int:study_id>/delete', methods=['POST'])
@login_required
def delete_study_from_container(container_id, study_id):
    user_id = session.get('user_id')
    study_service.remove_study_from_container(study_id, container_id, user_id)
    return redirect(url_for('view_container_cards', container_id=container_id))

@app.route('/admin/container/<int:container_id>/cards/<int:study_id>/edit', methods=['POST'])
@login_required
def edit_study_in_container(container_id, study_id):
    title = request.form.get('editCardTitle')
    content = request.form.get('editCardContent')
    user_id = session.get('user_id')
    if title and content:
        study_service.update_study(study_id, title, content, user_id)
    return redirect(url_for('view_container_cards', container_id=container_id))