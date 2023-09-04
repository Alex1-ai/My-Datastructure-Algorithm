

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("There is no element in the linkedList")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'

            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node

        itr = self.head

        while itr.next:
            itr = itr.next
        # when itr is None
        itr.next = Node(data, None)

    def insert_values(self, arrs):
        if self.head is None:
            self.head = None
            for arr in arrs:
                self.insert_at_end(arr)
        for arr in arrs:
            self.insert_at_end(arr)

    def get_length(self):
        if self.head is None:
            print("Empty LinkedList !!")

        itr = self.head
        # because you assign iter to one element in the linkedlist so count would be 1
        count = 0
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if (count == index-1):
                itr.next = itr.next.next

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            return "Invalid index"
        if index == 0:
            self.insert_at_begining(data)

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            count += 1
            itr = itr.next

    def remove_by_value(self, data):

        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if (itr.next.data == data):
                itr.next = itr.next.next
            itr = itr.next

    def insert_after_value(self, data_after, data):
        if self.head is None:
            return
        if self.head.data == data_after:
            node = Node(data, self.head.next)
            self.head.next = node

        itr = self.head
        while itr.next:
            if itr.data == data_after:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next


if __name__ == '__main__':
    pass

li = LinkedList()

li.insert_at_begining(5)
li.insert_at_begining(8)
li.remove_by_value('jug')
li.insert_at_end(78)
li.insert_values(['banana', 'pawpaw', 'pineapple', 'orange', 'mango'])
li.get_length()
li.print()
li.remove_at(2)
li.insert_at(2, 72)
li.insert_after_value('banana', 'orange')
li.insert_at(0, "beans")
li.remove_by_value('pineapple')
li.print()
