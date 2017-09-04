import psycopg2


class TaskService:

    def __init__(self):
        self.conn = psycopg2.connect("host='localhost' dbname='task' user='postgres' password='root'")
        print 'connect successful!'
        self.cursor = self.conn.cursor()

    def find(self):
        self.cursor.execute("select * from task where id>690")
        rows = self.cursor.fetchall()
        for row in rows:
            print 'id=', row[0], ',uuid=', row[1], ',description=', row[2], ',leaderid=', row[3], '\n'
        self.conn.close()

if __name__ == '__main__':
    svc = TaskService()
    svc.find()
