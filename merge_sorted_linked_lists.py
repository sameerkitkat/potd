# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create & Handle List operations
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to display the list
    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.data, end="->")
            temp = temp.next
        print(temp.data)

    # Method to add element to list
    def add_to_list(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode


# Function to merge the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def merge_lists(headA, headB):

    # A dummy node to store the result
    dummyNode = Node(0)

    # Tail stores the last node
    tail = dummyNode
    while True:

        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        # Advance the tail
        tail = tail.next

    # Returns the head of the merged list
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

