class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

class Linkedlist:

	def find_middle(self,head):
		fast = head
		slow = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			
		return slow.val

	def print_list(self,head):
		temp = head
		while temp.next:
			print(temp.val, end="->")
			temp = temp.next
		print(temp.val)




def main():
	node1 = Node(10)
	node2 = Node(20)
	node3 = Node(30)
	node4 = Node(40)
	node5 = Node(50)
	node6 = Node(60)
	node7 = Node(70)
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5
	node5.next = node6
	node6.next = node7
	linkedlist = Linkedlist()
	#linkedlist.print_list(node1)
	print(linkedlist.find_middle(node1))


if __name__ == '__main__':
	main()