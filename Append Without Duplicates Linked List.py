# Write a function to remove all duplicates from an unsorted singly linked list in-place using a hash table,
# preserving the original order of the remaining elements.

# The input will be a sequence of integers representing the elements of the linked list, ending with -1 to indicate the end of the list.
# The output should be the modified linked list with duplicates removed, printed as a space-separated sequence of integers.

#---------------------------------------------------#

# For example, if the input is 1 2 3 2 4 5  
# The output should be 1 2 3 4 5

#---------------------------------------------------#


#Append Without Duplicates
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates_hashing(head):
    seen = set()
    current = head
    prev = None
    while current:
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            prev = current
        current = current.next

def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next

# Example usage
if __name__ == "__main__":
    elements = list(map(int, input().split()))
    head = None
    for data in elements:
        if data == -1:
            break
        new_node = Node(data)
        if not head:
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node

    remove_duplicates_hashing(head)
    print_list(head)