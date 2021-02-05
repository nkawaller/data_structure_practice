class Tree:

    def __init__(self, value=None, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right

    def PrintTree(self):
        print(self.value)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()


r = Tree(8)
r.left = Tree(3)
r.right = Tree(10)
r.left.left = Tree(1)
r.left.right = Tree(6)
r.right.right = Tree(14)
r.PrintTree()