# Quieues
# FIFO = FIRST IN FIRST OUT
# methods in queues
# Enqueue(append) - add an item to the endo fo the line
# Dequeue(popleft) - remove an item from the first of the line

#from collections import deque
'''
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())
'''

class Queue:
    def __init__(self):
        self.queue = list()
    def Enqueue(self, item):
        self.queue.append(item)
    def Dequeue(self):
        if len(self.queue) > 0:
            return self.queue.remove(self.queue[0])
        
        else:
            return None
    def __str__(self):
        return str(self.queue)


myQueue = Queue()
myQueue.Enqueue(8)
myQueue.Enqueue(27)
myQueue.Enqueue(30)
myQueue.Enqueue(22)
print(myQueue)
myQueue.Dequeue()
myQueue.Dequeue()
print(myQueue)