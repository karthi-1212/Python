#Given a singly linked list of integers and position 'i', delete the node at the 'i-th' position recursively. 
#Input consists of the list elements separated by space, followed by the integer 'i'. 
#The output displays the updated list after the deletion operation has been performed.

#------------------------------------------------------#
#Sample Input 
#3 4 5 2 6 1 9 -1
#3
#output
#3 4 5 6 1 9
#------------------------------------------------------#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def deleteNode(head, position):
    if head is None:
        return head
    
    if position == 0:
        temp = head
        head = temp.next
        temp = None
        return head
    
    head.next = deleteNode(head.next, position - 1)
    return head

def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Input
elements = list(map(int, input().split()))
position = int(input())

# Create the linked list
head = None
prev = None
for element in elements:
    if element == -1:
        break
    new_node = Node(element)
    if head is None:
        head = new_node
    else:
        prev.next = new_node
    prev = new_node

# Delete the node at the given position
head = deleteNode(head, position)

# Output
printList(head)