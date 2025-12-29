#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     """ my initial attempt """
    #     res = []
    #     carry = 1
    #     for digit in digits[::-1]:
    #         val = digit + 1
    #         if val >= 10:
    #             carry = 1
    #             val = 1
    #         carry = val // 10
    #         val = val % 10
    #         res.append(val)
    #         if carry == 0:
    #             break

    #     return [res[:len(res)] , res[::-1]]
    
    def plusOne(self, digits: List[int]) -> List[int]:
        """ cracking Faang O(n), O(1) """
        carry = 1
        i = len(digits) - 1
        while i >= 0:
            cur = digits[i] + carry
            digits[i] = cur % 10
            carry = cur // 10

            if not carry:
                break
            i -= 1

        if carry:
            digits.insert(0, carry)
        
        return digits
        
# @lc code=end

# def plusOne(self, digits: List[int]) -> List[int]:
#         """ practice: cracking Faang O(n), O(1) """
#         carry = 1
#         i = len(digits) - 1
#         while i >= 0:
#             cur = digits[i] + carry
#             digits[i] = cur % 10
#             carry = cur // 10
#             if not carry:
#                 break
#             i -= 1
#         if carry:
#             digits.insert(0, carry)
#         return digits

