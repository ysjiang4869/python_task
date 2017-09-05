from flask import Flask, jsonify,Response
from org.uvlab.cloud.service.task.service.TaskService import TaskService
import json
import uuid
from sqlalchemy.orm.state import InstanceState
from datetime import datetime, date
app = Flask(__name__)
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


@app.route('/')
def hello_world():
    task = svc.get('c770c84d-71dc-4cfb-b5d4-215516dbd0c2')
    print task.__dict__
    # print json.dumps(task, cls=ComplexEncoder)
    res = json.dumps(task.__dict__, cls=ComplexEncoder)
    return Response(res, mimetype='application/json')

if __name__ == '__main__':
    print svc.get('c770c84d-71dc-4cfb-b5d4-215516dbd0c2')
    app.run()
