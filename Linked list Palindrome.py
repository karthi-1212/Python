# Given a singly linked list of integers, create a function to check if it is a palindrome. 
# Output 'true' if it is a palindrome, 'false' otherwise.

#-------------------------------------------#

#Sample Input 9 2 3 3 2 9 -1
#Sample Output true

#-------------------------------------------#

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def isPalindrome(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values == values[::-1]

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

# Take input from the user
input_values = list(map(int, input().split()))

# Create the singly linked list
head = createLinkedList(input_values)

# Check if the list is a palindrome
print(str(isPalindrome(head)).lower())

