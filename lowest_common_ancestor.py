class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def lowest_common_ancestor(self, root, p, q):
		parent_val = root.val
		p_val = p.val
		q_val = q.val

		if p_val > parent_val and q_val > parent_val:
			return self.lowest_common_ancestor(root.right,p,q)
		if p_val < parent_val and q_val < parent_val:
			return self.lowest_common_ancestor(root.left,p,q)
		else:
			return root

def main():
	node = Node(4)
	node.left = Node(2)
	node.right = Node(7)
	node.left.left = Node(1)
	node.left.right = Node(3)
	node.right.left = Node(6)
	node.right.right = Node(9)
	solution = Solution()
	ans = solution.lowest_common_ancestor(node, node.left.left, node.left)
	print(ans.val)

if __name__ == '__main__':
	main()