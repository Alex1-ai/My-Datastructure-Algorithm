# LEARNING STACK, HEAP , QUEUES, TREE

# Learning  STACK. 
# push : to put an item onto the stack
# pop . to pop an item off the stack.
# peek: get item on top of stack, without removing it
# clear: remove all the item in the stack
# it uses LIFO = last in first out

my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack)


print(my_stack.pop())
print(my_stack.pop())
print(my_stack)

# ADDING SOME FUNCTIONALITY TO THE STACK
class Stack:
    def __init__(self):
         self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    # shows you the last item
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)


my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
        


