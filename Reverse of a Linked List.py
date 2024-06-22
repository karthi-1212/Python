
# Given a sequence of integer values representing the nodes of a singly linked list, 
# where -1 indicates the end of the list, print the values of the nodes in reverse order.

#-------------------------------------------#

#Sample Input 1 3 54 
#Sample Output 54 3 1 

#-------------------------------------------#

#Print the reverse of a Linked List
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to create a singly linked list from input values
def createLinkedList(input_values):
    head = ListNode(input_values[0])
    current = head
    for value in input_values[1:]:
        if value == -1:
            break
        new_node = ListNode(value)
        current.next = new_node
        current = new_node
    return head

# Function to print the linked list in reverse order
def printReversedLinkedList(head):
    if head is None:
        return
    printReversedLinkedList(head.next)
    print(head.value, end=" ")

# Take input from the user
input_values = list(map(int, input().split()))

# Create the singly linked list
head = createLinkedList(input_values)

# Print the reversed linked list
printReversedLinkedList(head)
