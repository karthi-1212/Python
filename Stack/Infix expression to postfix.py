""" Convert the given infix expression to postfix .
Input Format

String having infix expression
Constraints

no

Output Format

Postfix expression

Sample Input 0

A+B*C+D
Sample Output 0

ABC*+D+
Sample Input 1

A+B*C/D-X
Sample Output 1

ABC*D/+X-"""

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = ''
    for char in expression:
        if char.isalnum():
            postfix += char
        elif char in precedence:
            while (stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[char]):
                postfix += stack.pop()
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
    while stack:
        postfix += stack.pop()
    return postfix

# Take input from the user
infix_expression = input()
print(infix_to_postfix(infix_expression))