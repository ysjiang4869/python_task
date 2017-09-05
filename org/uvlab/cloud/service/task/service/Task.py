from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/task'
db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    uuid = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.String(1024))
    deadline = db.Column(db.DateTime)
    rowstate = db.Column(db.Integer, nullable=False, default=1)
    leaderid = db.Column(db.String(40))
    crtdate = db.Column(db.DateTime, nullable=False, default=datetime.now())
    crtuser = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.String(128))
    priority = db.Column(db.Integer, nullable=False, default=0)
    importance = db.Column(db.Integer, nullable=False, default=0)
    urgency = db.Column(db.Integer, nullable=False, default=0)
    parentid = db.Column(db.String(40))
    upduser = db.Column(db.Integer, nullable=False)
    upddate = db.Column(db.DateTime, nullable=False, default=datetime.now())
    actbegindate = db.Column(db.DateTime)
    actbegintime = db.Column(db.DateTime)
    actenddate = db.Column(db.DateTime)
    actendtime = db.Column(db.DateTime)
    initiator = db.Column(db.String(64))
    linkobjecttype = db.Column(db.String(64))
    linkobject = db.Column(db.String(64))
    category = db.Column(db.Integer, nullable=False, default=0)
    objectstate = db.Column(db.Integer, nullable=False, default=0)
    durationtype = db.Column(db.Integer, nullable=False, default=0)
    repeatable = db.Column(db.Integer, nullable=False, default=0)
    repeatperiod = db.Column(db.Integer, nullable=False, default=0)
    expbegindate = db.Column(db.DateTime)
    expbegintime = db.Column(db.DateTime)
    expenddate = db.Column(db.DateTime)
    expendtime = db.Column(db.DateTime)
    percentage = db.Column(db.Integer, nullable=False, default=0)
    expcost = db.Column(db.Integer, nullable=False, default=0)
    actcost = db.Column(db.Integer, nullable=False, default=0)
    url = db.Column(db.String(128))
    color = db.Column(db.Integer)
    quality = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, description, crtuser, upduser):
        self.description = description
        self.uuid = uuid.uuid4()
        self.rowstate=1
        self.crtdate = datetime.now()
        self.upddate = datetime.now()
        self.crtuser = crtuser
        self.owner = [crtuser]
        self.upduser = upduser
        self.priority = 0
        self.importance = 0
        self.urgency = 0
        self.category = 0
        self.objectstate = 0
        self.durationtype = 4
        self.repeatable = 1
        self.repeatperiod = 0
        self.percentage = 0
        self.expcost = 0
        self.actcost = 0
        self.quality = 0

if __name__ == '__main__':
    task = Task("by python", 18, 18)
    task.repeatperiod=5
    # db.session.add(task)
    # db.session.commit()
    params = {'description': 'by python'}
    tasks = Task.query.filter_by(**params).order_by("crtdate desc").limit(10).offset(0).all()
    for item in tasks:
        print item.id
        print item.uuid
        # print item.owner[0]

