#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     """ my first attempt """
    #     count1 = {}
    #     count2 = {}

    #     for c in str1:
    #         count1[c] = count1.get(c, 0) + 1

    #     for c in str2:
    #         count2[c] = count2.get(c, 0) + 1

    #     if len(count1) != len(count2):
    #         return ""
        
    #     return "".join(count2.keys())
    
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     """ Approach 1: Brute Force O(min(m, n) . (m + n)), O(min(m, n)) """ 
    #     len1, len2 = len(str1), len(str2)
        
    #     def valid(k):
    #         if len1 % k or len2 % k: 
    #             return False
    #         n1, n2 = len1 // k, len2 // k
    #         base = str1[:k]
    #         return str1 == n1 * base and str2 == n2 * base 
        
    #     for i in range(min(len1, len2), 0, -1):
    #         if valid(i):
    #             return str1[:i]
    #     return ""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """ Approach 2: Greatest Common Divisor O(m + n), O(m + n) """
        # def gcd_fun(x, y):
        #     while(y):
        #         x, y = y, x % y
        #         return abs(x)
            
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""
        
        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        # max_length = gcd_fun(len(str1), len(str2))
        return str1[:max_length]


        
# @lc code=end

