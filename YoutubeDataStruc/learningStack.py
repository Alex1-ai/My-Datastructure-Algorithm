s = []
s.append('http://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('http://www.cnn.com/china')

print(s.pop())
print(s.pop())
print(s.pop())

# implementing stack with collections
from collections import deque
from ssl import SSL_ERROR_WANT_X509_LOOKUP
stack = deque()
# if you want to see the method of a class just write
dir(stack)

stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('http://www.cnn.com/china')


print(stack.pop)
print(stack.pop)



 # CREATING A STACK CLASS
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
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)



st =  Stack()
st.push(5)
st.peek()
st.pop()
st.is_empty()

