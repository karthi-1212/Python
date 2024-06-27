"""Implement a Queue Data Structure specifically to store integer data using a Singly Linked List.
The data members should be private.
You need to implement the following public functions :
Constructor:
It initialises the data members as required.
enqueue(data) :
This function should take one argument of type integer. It enqueues the element into the queue and returns nothing.
dequeue() :
It dequeues/removes the element from the front of the queue and in turn, returns the element being dequeued or removed. In case the queue is empty, it returns -1.
front() :
It returns the element being kept at the front of the queue. In case the queue is empty, it returns -1.
getSize() :
It returns the size of the queue at any given instance of time.
isEmpty() :
It returns a boolean value indicating whether the queue is empty or not.

Operations Performed on the Stack:

Query-1(Denoted by an integer 1): Enqueues an integer data to the queue.
Query-2(Denoted by an integer 2): Dequeues the data kept at the front of the queue and returns it to the caller.
Query-3(Denoted by an integer 3): Fetches and returns the data being kept at the front of the queue but doesn't remove it, unlike the dequeue function.
Query-4(Denoted by an integer 4): Returns the current size of the queue.
Query-5(Denoted by an integer 5): Returns a boolean value denoting whether the queue is empty or not.
Input Format

The first line contains an integer 'q' which denotes the number of queries to be run against each operation on the queue.
Then the test cases follow.
Every 'q' lines represent an operation that needs to be performed.
For the enqueue operation, the input line will contain two integers separated by a single space, representing the type of the operation in integer and the integer data being enqueued into the queue.
For the rest of the operations on the queue, the input line will contain only one integer value, representing the query being performed on the queue.
Constraints

1 <= q <= 10^5
1 <= x <= 5
-2^31 <= data <= 2^31 - 1 and data != -1
Where 'q' is the total number of queries being performed on the queue, 'x' is the range for every query and data represents the integer pushed into the queue.
Time Limit: 1 second
Output Format

For Query-1, you do not need to return anything.
For Query-2, prints the data being dequeued from the queue.
For Query-3, prints the data kept on the front of the queue.
For Query-4, prints the current size of the queue.
For Query-5, prints 'true' or 'false'(without quotes).
Output for every query will be printed in a separate line.
Sample Input 0

7
1 17
1 23
1 11
2
2
2
2
Sample Output 0

17
23
11
-1
Sample Input 1

3
2
1 10
4
Sample Output 1

-1 
1"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return -1
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None
        return data

    def front(self):
        if self.head is None:
            return -1
        return self.head.data

    def getsize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

if __name__ == "__main__":
    q = int(input())
    queue = Queue()
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            data = query[1]
            queue.enqueue(data)
        elif query[0] == 2:
            print(queue.dequeue())
        elif query[0] == 3:
            print(queue.front())
        elif query[0] == 4:
            print(queue.getsize())
        elif query[0] == 5:
            print(queue.isEmpty())