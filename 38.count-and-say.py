#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    # def countAndSay(self, n: int) -> str:
    #     """ Approach 1: Straightforward O(4 ^(n/3)), O(4 ^(n/3)) """
    #     current_string = "1"
    #     for _ in range(n - 1):
    #         next_string = ""
    #         j = 0
    #         k = 0
    #         while j < len(current_string):
    #             while (
    #                 k < len(current_string)
    #                 and current_string[k] == current_string[j]
    #             ):
    #                 k += 1
    #             next_string += str(k - j) + current_string[j]
    #             j = k
    #         current_string = next_string
    #     return current_string
    
    def countAndSay(self, n: int) -> str:
        """ Approach 2: Regular Expression  O(4 ^(n/3)), O(4 ^(n/3)) """
        s = "1"
        for _ in range(n - 1):
            # m.group(0) is the entire match, m.group(1) is its first digit
            s = re.sub(
                r"(.)\1*", lambda m: str(len(m.group(0))) + m.group(1), s
            )
        return s
    
# @lc code=end

