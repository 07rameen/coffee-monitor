from queue import  Queue
q = Queue()

def put_record(data: dict):
    q.put(data)

def get_record():
    return q.get()