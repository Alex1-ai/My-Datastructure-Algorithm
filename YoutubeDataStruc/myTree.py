class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = " "*self.get_level()*3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix, self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def build_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Windows'))
    laptop.add_child(TreeNode('Dell'))

    cellphone = TreeNode('cellphone')
    cellphone.add_child(TreeNode('iPhone'))
    cellphone.add_child(TreeNode('android'))
    cellphone.add_child(TreeNode('vivo'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('Toshiba'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_tree()
    root.print_tree()
