import json
import uuid
from datetime import datetime, date
import collections
from flask import Response, request, abort
from sqlalchemy.orm.state import InstanceState

from org.uvlab.cloud.service.task.service.Task import app, dict2task
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
    ret = collections.OrderedDict()
    for task in tasks:
        ret[str(task.uuid)] = task.__dict__
    return Response(json.dumps(ret, cls=ComplexEncoder), mimetype='application/json')


@app.route('/task/<uuid:task_id>', methods=['GET'])
def get(task_id):
    task = svc.get(task_id)
    if task is None:
        res = None
    else:
        res = json.dumps(task.__dict__, cls=ComplexEncoder)
    return Response(res, mimetype='application/json')


@app.route('/task', methods=['POST'])
def add():
    body = request.get_json(force=True)
    task = dict2task(body)
    task.crtuser = 18
    task.upduser = 18
    svc.add(task)
    res = json.dumps(task.__dict__, cls=ComplexEncoder)
    return Response(res, mimetype='application/json')


@app.route('/task/<uuid:task_id>', methods=['PUT'])
def update(task_id):
    body = request.get_json(force=True)
    if 'uuid' not in body:
        abort(404)
    if str(task_id) != str(body['uuid']):
        abort(500)
    svc.set(task_id, body)
    return Response(None, mimetype='application/json')


@app.route('/task/<uuid:task_id>', methods=['DELETE'])
def delete(task_id):
    svc.delete(task_id)
    return Response(None, mimetype='application/json')


def start():
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
