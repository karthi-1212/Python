#You are given a Linked List and you need to find the largest or maximum element that is present in the Linked List
#------------------------------------------------------------#

#Sample Input 1 2 3 4 5 -1
#Sample Output 5

#------------------------------------------------------------#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_max_element(head):
    max_element = float('-inf')  # Initialize max_element to negative infinity
    current = head

    while current is not None:
        if current.data > max_element:
            max_element = current.data
        current = current.next

    return max_element

# Parse the input and create the linked list
input_list = list(map(int, input().split()))
head = Node(input_list[0])
current = head
for data in input_list[1:]:
    if data == -1:
        break
    new_node = Node(data)
    current.next = new_node
    current = new_node

# Find the maximum element
max_element = find_max_element(head)
print(max_element)