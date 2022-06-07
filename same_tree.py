class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def isSameTree(p, q):
    if not p and not q:
        return True 
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.right, q.right)\
            and isSameTree(p.left, q.left)


def main():
    root1 = Node(10)
    root1.left = Node(20)
    root1.right = Node(30)
    root1.left.left = Node(40)
    root1.left.right = Node(60)

    root2= Node(10)
    root2.left = Node(20)
    root2.right = Node(30)
    root2.left.left = Node(40)
    root2.left.right = Node(60)

    print(isSameTree(root1,root2))



if __name__ == '__main__':
    main()
