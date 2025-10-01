from src.data.db_context import db

class StudyContainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    studies = db.relationship('Study', backref='container', lazy=True)

    def __repr__(self):
        return f"<StudyContainer {self.name}>"