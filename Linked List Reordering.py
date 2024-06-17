#Linked List Reordering is a process where the elements of a linked list are rearranged in an alternating fashion, 
#by splitting the list into two halves, reversing the second half, and then merging the two halves by alternating nodes. 
#This reordering technique changes the order of elements in the linked list while maintaining the original elements.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def reorderList(self):
        input_values = input("Enter the values for the linked list separated by spaces: ")
        values = list(map(int, input_values.split()))
        
        for value in values:
            self.insert(value)

        if self.head is None or self.head.next is None:
            return

        # Step 1: Find the middle of the linked list
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the linked list into two halves
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        head1, head2 = self.head, prev

        # Step 3: Merge the two halves in an alternating fashion
        while head2.next:
            head1.next, head1 = head2, head1.next
            head2.next, head2 = head1, head2.next

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
linked_list = LinkedList()
linked_list.reorderList()
linked_list.printList()