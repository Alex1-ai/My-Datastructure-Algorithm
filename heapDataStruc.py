# MAXHEAP IS FAST
# insert in O(log n)
# get Max in O(1)
# remove Max in O(log n)

# access the paraent of a node through the child
# i = 4
# parent(i) = i/2 = 2

# acess the child of a node throug the parent
# leftChild(i) = i * 2 = 8
# rightChild(i) = i * 2 + 1

# OPERATIONS IN MAP HEAPS 
# push(insert)
# peek(get max)
# pop (remove max)



class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)
    
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)
    

    # peak returns the at the index 1(highest value)
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False 
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j],self.heap[i]



    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)


m = MaxHeap([95,3,21])
m.push(10)
print(m)
print(m.pop())
print(m)
print(m.peek())



