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

    def __init__(task, description, crtuser, upduser):
        task.description = description
        task.uuid = uuid.uuid4()
        task.rowstate=1
        task.crtdate = datetime.now()
        task.upddate = datetime.now()
        task.crtuser = crtuser
        task.owner = [crtuser]
        task.upduser = upduser
        task.priority = 0
        task.importance = 0
        task.urgency = 0
        task.category = 0
        task.objectstate = 0
        task.durationtype = 4
        task.repeatable = 1
        task.repeatperiod = 0
        task.percentage = 0
        task.expcost = 0
        task.actcost = 0
        task.quality = 0

    def __repr__(task):
        return '<Task: %r>' % str(task.uuid)


def dict2task(d):
    task = Task(d.get('description'), d.get('crtuser'), d.get('upduser'))
    task.uuid = d.get('uuid')
    task.rowstate = d.get('rowstate', task.rowstate)
    task.crtdate = d.get('crtdate', task.crtdate)
    task.upddate = d.get('upddate', task.upddate)
    task.priority = d.get('priority', task.priority)
    task.importance = d.get('importance', task.importance)
    task.urgency = d.get('urgency', task.urgency)
    task.category = d.get('category', task.category)
    task.objectstate = d.get('objectstate', task.objectstate)
    task.durationtype = d.get('durationtype', task.durationtype)
    task.repeatable = d.get('repeatable', task.repeatable)
    task.repeatperiod = d.get('repeatperiod', task.repeatperiod)
    task.percentage = d.get('percentage', task.percentage)
    task.expcost = d.get('expcost', task.expcost)
    task.actcost = d.get('actcost', task.actcost)
    task.quality = d.get('quality', task.quality)
    return task


# if __name__ == '__main__':
#     task = Task("by python", 18, 18)
#     task.repeatperiod=5
#     # db.session.add(task)
#     # db.session.commit()
#     params = {'description': 'by python'}
#     tasks = Task.query.filter_by(**params).order_by("crtdate desc").limit(10).offset(0).all()
#     for item in tasks:
#         print item.id
#         print item.uuid
#         # print item.owner[0]

