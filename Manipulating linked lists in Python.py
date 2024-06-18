#First take a linkedList and then try to print that LinkedList
#Input Format Take LinkedList Input no Constraints and Output Format Print the LinkedList

#----------------------------------------------#
#Sample Input 0
#1 2 3 4 5 -1
#Sample Output 0
#1 2 3 4 5
#----------------------------------------------#

## OverView

#This Python code defines classes for Node and LinkedList. The Node class represents a node in a linked list with data and a pointer to the next node. 
#The LinkedList class manages the linked list, allowing for appending nodes and printing the list. 
#It takes user input to create a linked list and prints the elements until encountering a `-1`.

# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

# Take LinkedList input
input_list = list(map(int, input().split()))
linked_list = LinkedList()
for num in input_list:
    if num == -1:
        break
    linked_list.append(num)

# Print the LinkedList
linked_list.print_list()