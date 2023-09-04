from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return self.container == 0

    def size(self):
        return len(self.container)

    def reverse_string(self, val):
        reverse = ""
        count = len(val)-1
        for letter in val:
            reverse+=(val[count])
            count -= 1
        
        return reverse
    

s = Stack()
s.push(32)
s.push(12)
s.push(30)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.container)
print(s.is_empty())
print(s.size())
print(s.reverse_string('good'))