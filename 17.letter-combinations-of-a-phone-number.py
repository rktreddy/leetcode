#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
    #     """ Approach 1: Backtracking O(4^N,  ), O(N) """
    #     if len(digits) == 0:
    #         return []
        
    #     letters = {
    #         "2": "abc",
    #         "3": "def",
    #         "4": "ghi",
    #         "5": "jkl",
    #         "6": "mno",
    #         "7": "pqrs",
    #         "8": "tuv",
    #         "9": "wxyz"
    #     }
        
    #     def backtrack(index, path):
    #         # If the path is the same length as digits, we have a complete combination
    #         if len(path) == len(digits):
    #             combinations.append("".join(path))
    #             return #backtrack
            
    #         # Get the letters that the current digit maps to, and loop through them
    #         possible_letters = letters[digits[index]]
    #         for letter in possible_letters:
    #             # Add the letter to our current path
    #             path.append(letter)
    #             # Move on to the next digit
    #             backtrack(index + 1, path)
    #             # Backtrack by removing the letter before moving onto the next
    #             path.pop()

    #     # Initiate backtracking with an empty path and starting index of 0
    #     combinations = []
    #     backtrack(0, [])
    #     return combinations

    # def letterCombinations(self, digits: str) -> List[str]:
    #     " Top upvoted solution"
    #     """
    #     :type digits: str
    #     :rtype: List[str]
    #     """
    #     dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
    #     res=[]
    #     if len(digits) == 0:
    #         return res
            
    #     self.dfs(digits, 0, dic, '', res)
    #     return res
    
    # def dfs(self, nums, index, dic, path, res):
    #     if index >=len(nums):
    #         res.append(path)
    #         return
    #     string1 = dic[nums[index]]
    #     for i in string1:
    #         self.dfs(nums, index+1, dic, path + i, res)


    # def letterCombinations(self, digits: str) -> List[str]:
    #     " practice: Top upvoted solution"
    #     dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    #     def dfs(nums, index, dic, path, res):
    #         if index >= len(nums):
    #             res.append(path)
    #             return
    #         string1 = dic[nums[index]]
    #         for i in string1:
    #             dfs(nums, index + 1, dic, path + i, res)

    #     res = []
    #     if len(digits) == 0:
    #         return res 
        
    #     dfs(digits, 0, dic, "", res)
    #     return res

    # def letterCombinations(self, digits: str) -> List[str]:
    #     " practice: Top upvoted solution"
    #     dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    #     def dfs(nums, index, dic, path, res):
    #         if index >= len(nums):
    #             res.append(path)
    #             return
    #         string1 = dic[nums[index]]
    #         for i in string1:
    #             dfs(nums, index + 1, dic, path + i, res)

    #     res = []
    #     if len(digits) == 0:
    #         return res
    #     dfs(digits, 0, dic, "", res)
    #     return res
            
    # from typing import List

    # def letterCombinations(self, digits: str) -> List[str]:
    #     """ Algomonster  O(4^N,  ), O(N) """
    #     # If the input string is empty, return an empty list
    #     if not digits:
    #         return []
      
    #     # Mappings of digits to letters as found on a phone dialpad
    #     digit_to_chars = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
      
    #     # Initialize the list of combinations with an empty string
    #     combinations = ['']
      
    #     # Iterate through each digit in the input string
    #     for digit in digits:
    #         # Determine the corresponding letters from the mapping
    #         # Subtract 2 because 'abc' corresponds to digit '2'
    #         letters = digit_to_chars[int(digit) - 2]
          
    #         # Build new combinations by appending each possible letter to each existing combination
    #         combinations = [prefix + letter for prefix in combinations for letter in letters]
      
    #     # Return the list of all letter combinations
    #     return combinations
    
    def letterCombinations(self, digits: str) -> List[str]:
        """ practice: Algomonster: list comprehension O(4^N,  ), O(N) """
        if not digits:
            return []
        
        digit_to_chars = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        combinations = ['']
        for digit in digits:
            letters = digit_to_chars[int(digit) - 2]
            combinations = [prefix + letter for prefix in combinations for letter in letters]

        return combinations
        
# @lc code=end

