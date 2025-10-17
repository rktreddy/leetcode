#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """ Using built-in functions O(N+M)"""
        # return "{0:b}".format(int(a, 2) + int(b, 2))
        
        """ Approach 1: Bit-by-Bit Computation O(max(N, M)), O(max(N, M))"""
        # n = max(len(a), len(b))

        # a, b = a.zfill(n), b.zfill(n)

        # carry = 0
        # answer = [] 
        # for i in range(n-1, -1, -1):
        #     if a[i] == "1":
        #         carry += 1
        #     if b[i] == "1":
        #         carry += 1

        #     if carry % 2 == 1:
        #         answer.append("1")
        #     else:
        #         answer.append("0")

        #     carry //= 2

        # if carry == 1:
        #     answer.append("1")

        # answer.reverse()

        # return "".join(answer)

        """ practice: Approach 1: Bit-by-Bit Computation O(max(N, M)), O(max(N, M)) """
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                answer.append("1")
            else:
                answer.append("0")

            carry //= 2

        if carry % 2 == 1:
            answer.append("1")

        answer.reverse()
        return "".join(answer)


        # """ Approach 2: Bit Manipulation O(N+M), O(max(N, M))"""
        # x, y = int(a, 2), int(b, 2)
        # while y:
        #     answer = x ^ y
        #     carry = (x & y) << 1
        #     x, y = answer, carry
        # return bin(x)[2:]
    
        # """ practice: Approach 2: Bit Manipulation O(N+M), O(max(N, M))"""
        # x, y = int(a, 2), int(b, 2)
        # while y:
        #     answer = x ^ y
        #     carry = (x & y) << 1
        #     x, y = answer, carry
        # return bin(x)[2:]

# @lc code=end

