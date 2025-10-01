from src.data.db_context import db

class Study(db.Model):
    __tablename__ = 'studies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    container_id = db.Column(db.Integer, db.ForeignKey('study_container.id'), nullable=True)

    def __init__(self, title, description=None):
        self.title = title
        self.description = description

    def __repr__(self):
        return f"<Study {self.title}>"