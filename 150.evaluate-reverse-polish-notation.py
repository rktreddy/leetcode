#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens):
        """ same as last" Approach 2: Evaluate with Stack without lambda O(N), O(N) """

        stack = []
        operators = set(["+", "-", "*", "/"])
        
        for t in tokens:
            if t not in operators:
                stack.append(int(t))  # Push operands onto the stack
            else:
                r = stack.pop()  # Second operand
                l = stack.pop()  # First operand
                
                if t == "+":
                    stack.append(l + r)
                elif t == "-":
                    stack.append(l - r)
                elif t == "*":
                    stack.append(l * r)
                elif t == "/":
                    # Division needs to handle negative values correctly
                    if l * r < 0 and l % r != 0:
                        stack.append(l // r + 1)
                    else:
                        stack.append(l // r)
        
        return stack.pop()  # Return the result of the evaluation
    

    # def evalRPN(self, tokens):
    #     """ Approach 1: Reducing the List In-place with lambda O(n^2), O(1)"""
    #     operations = {
    #         "+": lambda a, b: a + b,
    #         "-": lambda a, b: a - b,
    #         "/": lambda a, b: int(a / b),
    #         "*": lambda a, b: a * b,
    #     }

    #     current_position = 0

    #     while len(tokens) > 1:

    #         # Move the current position pointer to the next operator.
    #         while tokens[current_position] not in "+-*/":
    #             current_position += 1

    #         # Extract the operator and numbers from the list.
    #         operator = tokens[current_position]
    #         number_1 = int(tokens[current_position - 2])
    #         number_2 = int(tokens[current_position - 1])

    #         # Calculate the result to overwrite the operator with.
    #         operation = operations[operator]
    #         tokens[current_position] = operation(number_1, number_2)

    #         # Remove the numbers and move the pointer to the position
    #         # after the new number we just added.
    #         tokens.pop(current_position - 2)
    #         tokens.pop(current_position - 2)
    #         current_position -= 1

    #     return int(tokens[0])
    

    # def evalRPN(self, tokens):
    #     """ Approach 1: Reducing the List In-place without lambda O(n^2), O(1) """
    #     current_position = 0

    #     while len(tokens) > 1:

    #         # Move the current position pointer to the next operator.
    #         while tokens[current_position] not in "+-*/":
    #             current_position += 1

    #         # Extract the operator and numbers from the list.
    #         operator = tokens[current_position]
    #         number_1 = int(tokens[current_position - 2])
    #         number_2 = int(tokens[current_position - 1])

    #         # Calculate the result to overwrite the operator with.
    #         if operator == "+":
    #             tokens[current_position] = number_1 + number_2
    #         elif operator == "-":
    #             tokens[current_position] = number_1 - number_2
    #         elif operator == "*":
    #             tokens[current_position] = number_1 * number_2
    #         else:
    #             tokens[current_position] = int(number_1 / number_2)

    #         # Remove the numbers and move the pointer to the position
    #         # after the new number we just added.
    #         tokens.pop(current_position - 2)
    #         tokens.pop(current_position - 2)
    #         current_position -= 1

    #     return int(tokens[0])
    
    # def evalRPN(self, tokens):
    #     """ Approach 2: Evaluate with Stack with lambda O(N), O(N) """
    #     operations = {
    #         "+": lambda a, b: a + b,
    #         "-": lambda a, b: a - b,
    #         "/": lambda a, b: int(a / b),
    #         "*": lambda a, b: a * b,
    #     }

    #     stack = []
    #     for token in tokens:
    #         if token in operations:
    #             number_2 = stack.pop()
    #             number_1 = stack.pop()
    #             operation = operations[token]
    #             stack.append(operation(number_1, number_2))
    #         else:
    #             stack.append(int(token))
    #     return stack.pop()

    # def evalRPN(self, tokens):
    #     """ Approach 2: Evaluate with Stack without lambda O(N), O(N) """
    #     stack = []

    #     for token in tokens:
    #         if token not in "+-/*":
    #             stack.append(int(token))
    #             continue

    #         number_2 = stack.pop()
    #         number_1 = stack.pop()

    #         result = 0
    #         if token == "+":
    #             result = number_1 + number_2
    #         elif token == "-":
    #             result = number_1 - number_2
    #         elif token == "*":
    #             result = number_1 * number_2
    #         else:
    #             result = int(number_1 / number_2)

    #         stack.append(result)

    #     return stack.pop()

        
# @lc code=end

