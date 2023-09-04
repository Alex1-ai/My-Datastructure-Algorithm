class Stack:
    def __init__(self, size):
        self.arr = size * [None]
        self.arrCapacity = size
        self.top = -1

        print(self.arr)

    def push(self, value):
        if self.isFull():
            print('Stack is full ')
            exit[-1]

        self.top = self.top + 1
        self.arr[self.top] = value
        return self.arr

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return -1

        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
            return -1

        return self.arr[self.top]

    def size(self):
        return self.top + 1

    def isFull(self):
        return self.size == self.arrCapacity

    def isEmpty(self):
        return self.size == 0


if __name__ == '__main__':
    d = Stack(5)
    print(d.isEmpty())

    # print(d.push(3))
    # print(d.push(4))
    # print(d.push(5))
    # print(d.pop())
    # print(d.push(6))
    print(d.peek())
    print(d)
