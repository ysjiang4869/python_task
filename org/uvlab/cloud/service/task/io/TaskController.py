import json
import uuid
from datetime import datetime, date

from flask import Response, request
from sqlalchemy.orm.state import InstanceState

from org.uvlab.cloud.service.task.service.Task import app, Task
from org.uvlab.cloud.service.task.service.TaskService import TaskService

svc = TaskService()


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        elif isinstance(obj, InstanceState):
            return None
        else:
            return json.JSONEncoder.default(self, obj)


@app.route('/task', methods=['GET'])
def find():
    offset = request.args.get('offset')
    if offset is None:
        offset = 0
    limit = request.args.get('limit')
    if limit is None:
        limit = 100
    desc = request.args.get('desc')
    if desc is None:
        desc = True
    order = request.args.get('order')
    if order is None:
        order = "crtdate"
    args = request.args.to_dict()
    keys_to_remove = ['offfset', 'limit', 'desc', 'order']
    for key in keys_to_remove:
        try:
            del args[key]
        except KeyError:
            pass
    tasks = svc.find(offset, limit, order, desc, **args)
    ret = {}
    for task in tasks:
        ret[str(task.uuid)] = task.__dict__
    return Response(json.dumps(ret, cls=ComplexEncoder), mimetype='application/json')


@app.route('/task/<uuid:task_id>', methods=['GET'])
def get(task_id):
    print str(task_id)
    task = svc.get('c770c84d-71dc-4cfb-b5d4-215516dbd0c2')
    res = json.dumps(task.__dict__, cls=ComplexEncoder)
    return Response(res, mimetype='application/json')


@app.route('/task', methods=['POST'])
def add():
    body = request.get_json(force=True)
    task = {}
    for k, v in body.items():
        task[str(k)] = str(v)
    # svc.add(task)
    print task


def start():
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
