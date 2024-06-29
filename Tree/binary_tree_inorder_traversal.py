"""
Take Input Level Wise of Binary Tree and then print in the inorder format

Input Format

No

Constraints

No

Output Format

Inorder traversal of Binary tree

Sample Input 0

8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
Sample Output 0

1 3 4 6 7 8 10 13 14
Sample Input 1

1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
Sample Output 1

4 2 5 1 6 3 7 
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def print_inorder(root):
    if root is None:
        return
 
    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)
 
if __name__ == "__main__":
    input_values = list(map(int, input().split()))  # Read space-separated input values
 
    root_val = input_values[0]
    root = TreeNode(root_val)
 
    q = []
    q.append(root)
 
    i = 1
    while q:
        node = q.pop(0)
        left_val = input_values[i]
        if left_val != -1:
            node.left = TreeNode(left_val)
            q.append(node.left)
 
        i += 1
        if i < len(input_values):
            right_val = input_values[i]
            if right_val != -1:
                node.right = TreeNode(right_val)
                q.append(node.right)
 
        i += 1  # Increment i after assigning both left and right child values
 
    print_inorder(root)