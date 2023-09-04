wmt = []
wmt.insert(0, 131.10)
wmt.insert(0,132.12)
wmt.insert(0,135)

print(wmt)

print(wmt.pop())
print(wmt.pop())

from collections import deque
q = deque()

q.appendleft(3)
q.appendleft(8)
q.appendleft(20)
q.appendleft(21)

q.pop()


class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


pq = Queue()

pq.enqueue({
    'company':'Wall Mart',
    'timestamp': '15 apr,11.01 AM',
    'price': 131.10
})

pq.enqueue({
    'company':'Wall Mart',
    'timestamp':'15 apr, 11.02 AM',
    'price': 132
})

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})


print(pq.buffer)

pq.dequeue()