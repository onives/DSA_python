class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self  # making the current node the parent of the child being added, dhaaa !!
        self.children.append(child)  # adding the child to the children list

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:  # while parent has a parent ==> parent not None
            level += 1
            p = p.parent
        return level


root = TreeNode("Electronics")
laptops = TreeNode("Laptops")
cell_phones = TreeNode("Cell Phones")
television = TreeNode("Televisions")

laptops.add_child(TreeNode("Macbook"))
laptops.add_child(TreeNode("Lenovo"))

cell_phones.add_child(TreeNode("iPhone"))
cell_phones.add_child(TreeNode("Android"))

television.add_child(TreeNode("LG"))
television.add_child(TreeNode("Sony"))

root.add_child(laptops)
root.add_child(cell_phones)
root.add_child(television)

root.print_tree()
