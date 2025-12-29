#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    # def addStrings(self, num1: str, num2: str) -> str:
    #     """ Approach 1: Elementary Math O(max (n1, n2)), O(max(n1, n2)) """
    #     res = []

    #     carry = 0
    #     p1 = len(num1) - 1
    #     p2 = len(num2) - 1
    #     while p1 >= 0 or p2 >= 0:
    #         x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
    #         x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
    #         value = (x1 + x2 + carry) % 10
    #         carry = (x1 + x2 + carry) // 10
    #         res.append(value)
    #         p1 -= 1
    #         p2 -= 1
        
    #     if carry:
    #         res.append(carry)
        
    #     return ''.join(str(x) for x in res[::-1])
    
    def addStrings(self, num1: str, num2: str) -> str:
        """ practice: Approach 1: Elementary Math O(max (n1, n2)), O(max(n1, n2)) """
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            val1 = ord(num1[i]) - ord('0') if i >= 0 else 0 # or use int(num1[i])
            val2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            res.append(val)

            i -= 1
            j -= 1
        if carry:
            res.append(carry)
            
        return ''.join(str(x) for x in res[::-1])

        
# @lc code=end

