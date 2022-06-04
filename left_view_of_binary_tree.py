class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LeftView(root):
    result = []
    level = []
    queue = [root]
    while queue != [] and root is not None:
        for node in queue:
            if node.right:
                level.append(node.right)
            if node.left:
                level.append(node.left)
            '''if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)'''
        result.append(node.data)
        queue = level
        level = []
    return result


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)
'''root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)'''

res = LeftView(root)
print(res)
