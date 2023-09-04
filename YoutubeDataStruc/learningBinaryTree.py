from msilib import datasizemask


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # checking if the data already exist
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                # this means you have a data in the left sub tree
                self.left.add_child(data)
            else:
                # means you are in leaf Node(last node)
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

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

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            # checking if data is in the left
            if self.left:
                return self.left.search(val)

            else:
                return False

        if val > self.data:
            # val might be in right subtree
            # checkin if data in my r
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    # range starting from 1 because you dont wont to add the
    # root two times
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))

    countries = ['India', 'Pakistan', 'Germany',
                 'USA', 'China', 'India', 'UK', 'USA']
    country_tree = build_tree(countries)

    print('UK is in the list? ', country_tree.search('UK'))
    print("Sweden is in the list? ", country_tree.search('Sweeden'))
    print(country_tree.in_order_traversal())
