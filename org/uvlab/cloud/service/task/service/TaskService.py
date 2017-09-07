from Task import Task, db
import uuid
from datetime import datetime


class TaskService:

    def __init__(self):
        self.db = db

    def add(self, task):
        task.uuid = uuid.uuid1()
        db.session.add(task)
        db.session.commit()
        return self.get(task.uuid)

    def find(self, offset, limit, order, desc, **params):
        if desc:
            orders = order + " desc"
        else:
            orders = order
        filters = ()
        for key, value in params.items():
            if key == 'description':
                filters = filters + (Task.description.like('%'+value+'%'),)
        return Task.query.filter(*filters).order_by(orders).limit(limit).offset(offset).all()

    def get(self, uuid):
        task = Task.query.filter_by(uuid=uuid).first()
        return task

    def set(self, uuid, task):
        try:
            del task['id']
            del task['uuid']
            del task['_sa_instance_state']
        except KeyError:
            pass
        task['upddate'] = datetime.now()
        Task.query.filter_by(uuid=uuid).update(task)
        db.session.commit()

    def delete(self, uuid):
        task = self.get(uuid)
        db.session.delete(task)
        db.session.commit()
