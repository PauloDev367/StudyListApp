from flask import render_template, request, redirect, url_for, session
from src.data.db_context import app
from src.middleware.auth_middleware import login_required 
from src.services.study_service import StudyService
from src.services.study_container_service import StudyContainerService

study_service = StudyService()
study_container_service = StudyContainerService()

@app.route('/admin/container/<int:container_id>/cards')
@login_required
def view_container_cards(container_id):
    user_id = session.get('user_id')
    container = study_container_service.get_container_by_id(container_id, user_id)
    if not container:
        return redirect(url_for('containers'))
    studies = study_service.get_all_container_studies(container_id, user_id)
    return render_template('study/study_cards.html', container=container, studies=studies)

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
    study_service.delete_study(study_id, user_id)
    return redirect(url_for('view_container_cards', container_id=container_id))

@app.route('/admin/container/<int:container_id>/cards/<int:study_id>/edit', methods=['POST'])
@login_required
def edit_study_in_container(container_id, study_id):
    title = request.form.get('name')
    content = request.form.get('description')
    link = request.form.get('link')
    user_id = session.get('user_id')
    status = request.form.get('status')
    if title and content:
        study_service.update_study(study_id, title, content, user_id, link, status)
    return redirect(url_for('view_container_cards', container_id=container_id))

@app.route('/admin/container/<int:container_id>/cards/<int:study_id>')
@login_required
def view_study_details(container_id, study_id):
    user_id = session.get('user_id')
    study = study_service.get_study_by_id(study_id, user_id)
    if not study or study.container_id != container_id:
        return redirect(url_for('view_container_cards', container_id=container_id))
    return {
        'id': study.id,
        'title': study.title,
        'description': study.description,
        'link': study.link,
        'status': study.status
    }