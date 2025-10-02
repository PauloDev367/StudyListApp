from src.models.study_container import StudyContainer
from src.models.study import Study
from src.models.user import User
from src.data.db_context import db

class StudyContainerService:
    @staticmethod
    def create_container(name, description, user_id):
        new_container = StudyContainer(name=name, description=description, user_id=user_id)
        db.session.add(new_container)
        db.session.commit()
        return new_container
    
    @staticmethod
    def get_all_containers(user_id):
        return StudyContainer.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_container_by_id(container_id, user_id):
        return StudyContainer.query.filter_by(id=container_id, user_id=user_id).first()
    
    @staticmethod
    def add_study_to_container(container_id, study_id, user_id):
        container = StudyContainerService.get_container_by_id(container_id, user_id)
        study = Study.query.get(study_id)
        if container and study:
            container.studies.append(study)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def remove_study_from_container(container_id, study_id, user_id):
        container = StudyContainerService.get_container_by_id(container_id, user_id)
        study = Study.query.get(study_id)
        if container and study and study in container.studies:
            container.studies.remove(study)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def delete_container(container_id, user_id):
        container = StudyContainerService.get_container_by_id(container_id, user_id)
        if container:
            db.session.delete(container)
            db.session.commit()
            return True
        return False