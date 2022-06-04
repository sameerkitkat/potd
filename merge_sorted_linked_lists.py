class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.data, end="->")
            temp = temp.next
        print(temp.data)

    def add_to_list(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode


def merge_lists(headA, headB):

   dummyNode = Node(0)

    tail = dummyNode
    while True:

        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        tail = tail.next

    return dummyNode.next



listA = LinkedList()
listB = LinkedList()


listA.add_to_list(5)
listA.add_to_list(10)
listA.add_to_list(15)

listB.add_to_list(2)
listB.add_to_list(3)
listB.add_to_list(20)


listA.head = merge_lists(listA.head, listB.head)

print("Merged Linked List is:")
listA.print_list()

