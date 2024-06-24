
# To reverse a singly linked list of integers 'k' at a time, ensuring that if the number of nodes is not a multiple of 'k,' 
# the remaining nodes are also reversed at the end.

#Example : 
#Given this linked list: 1 -> 2 -> 3 -> 4 -> 5, For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5,For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4
#Sample Input 1 2 3 4 5 6 7 8 9 10 -1
#4
#Sample Output 4 3 2 1 8 7 6 5 10 9

#Sample Input 1 2 3 4 5 -1 
#0
#Sample Output 1 2 3 4 5

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_k_nodes(head, k):
    if k <= 1:  # If k is 0 or 1, no need to reverse
        return head
    
    current = head
    next_node = None
    prev = None
    count = 0

    # Reverse first k nodes of the linked list
    while current is not None and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1

    # Recursively call for the rest of the list and link the new head to the next reversed group
    if next_node is not None:
        head.next = reverse_k_nodes(next_node, k)

    return prev

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" ")
        current = current.next

# Input
input_list = list(map(int, input().split()))
k = int(input())

head = ListNode(input_list[0])
current = head
for data in input_list[1:]:
    if data == -1:
        break
    node = ListNode(data)
    current.next = node
    current = node

# Reversing in groups of k
head = reverse_k_nodes(head, k)

# Output
print_linked_list(head)