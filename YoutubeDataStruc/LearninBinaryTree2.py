from xml.dom.minidom import Element


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return self.data == val

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search()

            else:
                return False

    def pre_order_traversal(self):
        element = []

        element.append(self.data)

        if self.left:
            element += self.left.pre_order_traversal()

        if self.right:
            element += self.right.pre_order_traversal()

        return element

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def calculate_sum(self):
        sum = 0

        if self.left:
            sum += self.left.calculate_sum()

        sum += self.data

        if self.right:
            sum += self.right.calculate_sum()

        return sum

    def in_order_traversal(self):
        # in order state that you visit your left then base and  then right
        elements = []

        if self.left:
            # visit left tree
            elements += self.left.in_order_traversal()
        # visit base
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [9, 2, 3, 9, 1, 5, 4, 3, 8]
    root = build_tree(numbers)
    print(root.post_order_traversal())
    print(root.pre_order_traversal())
    print(root.calculate_sum())
    print(root.find_max())
    print(root.find_min())
    print(root.delete(9))
