class Node:
	
	def __init__(self,val=0,left=None,right=None):
		self.val = val
		self.left = None
		self.right = None

class Solution:
	
	def max_depth(self,root):
		if root is None:
			return 0
		else:
			left_height = self.max_depth(root.left)
			right_height = self.max_depth(root.right)
			return max(left_height,right_height)+1


def main():
	node = Node(10)
	node.left = Node(9)
	node.right = Node(20)
	node.right.left = Node(15)
	node.right.right = Node(7)
	node.right.right.left = Node(5)
	sol = Solution()
	print(sol.max_depth(node))


if __name__ == '__main__':
	main()