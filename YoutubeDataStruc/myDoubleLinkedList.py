class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Empty DoubleLinked List")
            return
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data) + '-->'
                itr = itr.next

            print(llstr)

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, None, None)
            self.head = node

        else:
            itr = self.head
            node = Node(data, itr, None)
            # making it previous point at node
            itr.prev = node
            # change the head
            self.head = node

    def get_last_node(self):
        itr = self.head
        while itr.next:

            itr = itr.next

        return itr

    def print_backward(self):
        if self.head == None:
            print("Empty DoubleLinkedList")
            return
        itr = self.get_last_node()
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev

        print('printing the DBList backward', llstr)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(data, None, itr)
        itr.next = node

    def get_length(self):
        if self.head is None:
            print("Empty DBlist")
            return
        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_values(self, datas):
        self.head = Node
        for data in datas:
            self.insert_at_end(data)

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('index Error')
            return

        if index == 0:
            # self.insert_at_begining(data)
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
            return

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                    break
                itr.next = node

                break
            itr = itr.next
            count += 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

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


dl = DoubleLinkedList()
dl.insert_at_begining(7)
dl.insert_at_begining(8)
dl.insert_at_begining(20)
dl.insert_at_begining('jude')
dl.insert_at_end(30)
dl.insert_at_index(5, 'boy')
dl.print_forward()
dl.remove_by_value(20)
dl.remove_at_index(0)
dl.print_forward()

# dl.print_backward()
dl.get_length()
