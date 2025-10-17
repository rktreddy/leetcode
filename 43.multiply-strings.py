#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    # def multiply(self, num1: str, num2: str) -> str:
    #     """ Approach 1: Elementary Math O(M^2 + M N), O(M^2 + M N) """
    #     if num1 == "0" or num2 == "0":
    #         return "0"

    #     # Reverse both numbers.
    #     first_number = num1[::-1]
    #     second_number = num2[::-1]

    #     # For each digit in second_number, multipy the digit by first_number and then
    #     # store the multiplication result (reversed) in the results array.
    #     results = []
    #     for index, digit in enumerate(second_number):
    #         results.append(self.multiply_one_digit(digit, index, first_number))

    #     # Add all of the results together to get our final answer (in reverse order)
    #     answer = self.sum_results(results)

    #     # Reverse answer and join the digits to get the final answer.
    #     return "".join(str(digit) for digit in reversed(answer))

    # def multiply_one_digit(
    #     self, digit2: str, num_zeros: int, first_number: List[str]
    # ) -> List[int]:
    #     """Multiplies first_number by a digit from second_number (digit2)."""
    #     # Insert zeros at the beginning of the current result based on the current digit's place.
    #     current_result = [0] * num_zeros
    #     carry = 0

    #     # Multiply each digit in first_number with the current digit of the second_number.
    #     for digit1 in first_number:
    #         multiplication = int(digit1) * int(digit2) + carry
    #         # Set carry equal to the tens place digit of multiplication.
    #         carry = multiplication // 10
    #         # Append last digit to the current result.
    #         current_result.append(multiplication % 10)

    #     if carry != 0:
    #         current_result.append(carry)
    #     return current_result

    # def sum_results(self, results: List[List[int]]) -> List[int]:
    #     # Initialize answer as a number from results.
    #     answer = results.pop()

    #     # Add each result to answer one at a time.
    #     for result in results:
    #         new_answer = []
    #         carry = 0

    #         # Sum each digit from answer and result. Note: zip_longest is the
    #         # same as zip, except that it pads the shorter list with fillvalue.
    #         for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
    #             # Add current digit from both numbers.
    #             curr_sum = digit1 + digit2 + carry
    #             # Set carry equal to the tens place digit of curr_sum.
    #             carry = curr_sum // 10
    #             # Append the ones place digit of curr_sum to the new answer.
    #             new_answer.append(curr_sum % 10)

    #         if carry != 0:
    #             new_answer.append(carry)

    #         # Update answer to new_answer which equals answer + result
    #         answer = new_answer

    #     return answer
    
    
    # def multiply(self, num1: str, num2: str) -> str:
    #     """ Approach 2: Elementary math using less intermediate space O(M(M+N)), O(N+M) """
    #     if num1 == "0" or num2 == "0":
    #         return "0"

    #     # Reverse both numbers.
    #     first_number = num1[::-1]
    #     second_number = num2[::-1]

    #     # To store the multiplication result of each digit of secondNumber with firstNumber.
    #     N = len(first_number) + len(second_number)
    #     answer = [0] * N

    #     # Multiply each digit in second_number by the first_number
    #     # and add each result to answer
    #     for index, digit in enumerate(second_number):
    #         answer = self.addStrings(
    #             self.multiplyOneDigit(first_number, digit, index), answer
    #         )

    #     # Pop excess zero from the end of answer (if any).
    #     if answer[-1] == 0:
    #         answer.pop()

    #     # Ans is in the reversed order.
    #     # Reverse it to get the final answer.
    #     answer.reverse()
    #     return "".join(str(digit) for digit in answer)

    # def multiplyOneDigit(self, first_number: str, digit2: str, num_zeros: int):
    #     # Insert 0s at the beginning based on the current digit's place.
    #     currentResult = [0] * num_zeros
    #     carry = 0

    #     # Multiply firstNumber with the current digit of secondNumber.
    #     for digit1 in first_number:
    #         multiplication = int(digit1) * int(digit2) + carry
    #         # Set carry equal to the tens place digit of multiplication.
    #         carry = multiplication // 10
    #         # Append the ones place digit of multiplication to the current result.
    #         currentResult.append(multiplication % 10)

    #     if carry != 0:
    #         currentResult.append(carry)
    #     return currentResult

    # def addStrings(self, result: list, answer: list) -> list:
    #     carry = 0
    #     i = 0
    #     new_answer = []
    #     for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
    #         # Add current digits of both numbers.
    #         curr_sum = digit1 + digit2 + carry
    #         carry = curr_sum // 10
    #         # Append last digit of curr_sum to the answer.
    #         new_answer.append(curr_sum % 10)
    #         i += 1

    #     return new_answer
    
    # def multiply(self, num1: str, num2: str) -> str:
    #     """ Neetcode: multiplication O(M*N), O(N+M) """
    #     if "0" in [num1, num2]:
    #         return "0"

    #     res = [0] * (len(num1) + len(num2))
    #     num1, num2 = num1[::-1], num2[::-1]
    #     for i1 in range(len(num1)):
    #         for i2 in range(len(num2)):
    #             digit = int(num1[i1]) * int(num2[i2])
    #             res[i1 + i2] += digit
    #             res[i1 + i2 + 1] += res[i1 + i2] // 10
    #             res[i1 + i2] = res[i1 + i2] % 10

    #     res, beg = res[::-1], 0
    #     while beg < len(res) and res[beg] == 0:
    #         beg += 1
    #     res = map(str, res[beg:])
    #     return "".join(res)
    
    def multiply(self, num1: str, num2: str) -> str:
        """ practice: Neetcode: multiplication O(M*N), O(N+M) """
        if "0" in [num1, num2]:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res) 

# @lc code=end

