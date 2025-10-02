from src.models.study_container import StudyContainer
from src.models.study import Study
from src.models.user import User
from src.data.db_context import db

class StudyService:
    def get_all_container_studies(self, container_id, user_id):
        return Study.query.filter_by(container_id=container_id, user_id=user_id).all()

    def create_study(self, title, description, link, container_id, user_id):
        new_study = Study(title=title, description=description, link=link, container_id=container_id, status='new', user_id=user_id)
        db.session.add(new_study)
        db.session.commit()
        return new_study

    def get_study_by_id(self, study_id, user_id):
        return Study.query.filter_by(id=study_id, user_id=user_id).first()

    def update_study(self, study_id, title, content, user_id):
        study = self.get_study_by_id(study_id, user_id)
        if study:
            study.title = title
            study.content = content
            db.session.commit()
        return study

    def delete_study(self, study_id, user_id):
        study = self.get_study_by_id(study_id, user_id)
        if study:
            db.session.delete(study)
            db.session.commit()
        return study