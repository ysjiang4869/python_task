import uuid
import time


class Task:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.description = ''
        self.deadline = time.localtime()
        self.rowstate = 1
        self.leaderid = ''
        self.leaderName = ''
        self.crtdate = time.localtime()
        self.crtuser = 0
        self.owner = []
        self.prioroty = 0
        self.importance = 0
        self.urgency = 0
        self.parentid = ''
        self.upduser = ''
        self.upddate = time.localtime()
        self.actbegindate = ''
        self.actenddate = ''
        self.actbegintime = ''
        self.actendtime = ''
        self.initiator = ''
        self.linkobjecttype = ''
        self.linkobject = ''
        self.category = 0
        self.objectstate = 1
        self.durationtype = 4
        self.repeatable = 1
        self.repeatpriod = 0
        self.expbegintime = ''
        self.expbegindate = ''
        self.expenddate = ''
        self.expendtime = ''
        self.percentage = 0
        self.expcost = 0
        self.actcost = 0
        self.url = ''
        self.color = ''
        self.quality = ''
