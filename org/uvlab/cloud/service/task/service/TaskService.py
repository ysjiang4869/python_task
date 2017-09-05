from Task import Task
from Task import db


class TaskService:

    def __init__(self):
        self.db = db

    def add(self, task):
        db.session.add(task)
        db.session.commit()

    def find(self, offset, limit, order, desc, **params):
        if desc:
            orders = order + "desc"
        else:
            orders = order
        return Task.query.filter_by(**params).order_by(orders).limit(limit).offset(offset).all()

    def get(self, uuid):
        task = Task.query.filter_by(uuid=uuid).first()
        return task
