from src.data.db_context import db, app
import src.models

with app.app_context():
    db.create_all()

import src.routes

if __name__ == '__main__':
    app.run(debug=True)
