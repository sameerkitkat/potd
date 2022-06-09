class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def invert_tree(self,root):
		if not root:
			return None

		left = self.invert_tree(root.left)
		right = self.invert_tree(root.right)

		root.left = right
		root.right = left 
		return root

	def print_inorder(self,node):
		if node:
			print(node.val,end=" ")
			self.print_inorder(node.left)			
			self.print_inorder(node.right)


def main():
	node = Node(4)
	node.left = Node(2)
	node.right = Node(7)
	node.left.left = Node(1)
	node.left.right = Node(3)
	node.right.left = Node(6)
	node.right.right = Node(9)
	solution = Solution()
	print("Before inversion")
	solution.print_inorder(node)
	print()
	print("After inversion")
	solution.invert_tree(node)
	solution.print_inorder(node)

if __name__ == '__main__':
	main()