from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/task'
db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=False)

    def __init__(self, description):
        self.description = description


if __name__ == '__main__':
    task = Task("by python")
    # db.session.add(task)
    # db.session.commit()
    tasks = Task.query.all()
    for item in tasks:
        print item.id
