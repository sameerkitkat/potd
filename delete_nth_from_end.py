class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def print_list(self, head):
		temp = head 
		while temp.next:
			print(temp.data, end="->")
			temp = temp.next
		print(temp.data)

	def get_count(self, head):
		temp = head
		count = 0 
		while temp:
			temp = temp.next
			count += 1
		return count


	def delete_nth_from_end(self, head, n):
		total = self.get_count(head)
		
		if n == 0:
			return head

		if n == total:
			head = head.next
			return head 

		k = total - n - 1
		c = 0
		temp = head

		while c != k:
			temp = temp.next
			c+=1
		temp.next = temp.next.next
		return head

	'''def delete_nth_from_end(self, head, n):
		fast = head
		slow = head
		total = self.get_count(head)
		if n == 0:
			return head

		if n == total:
			head = head.next
			return head 

		count = 0
		while count != n:
			fast = fast.next
			count += 1

		while fast.next:
			fast = fast.next
			slow = slow.next

		slow.next = slow.next.next

		return head'''


def main():
	linkedlist = LinkedList()

	node1 = Node(10)
	node2 = Node(20)
	node3 = Node(30)
	node4 = Node(40)
	node5 = Node(50)

	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5

	linkedlist.print_list(node1)
	head = linkedlist.delete_nth_from_end(node1, 5)
	linkedlist.print_list(head)


if __name__ == '__main__':
	main()