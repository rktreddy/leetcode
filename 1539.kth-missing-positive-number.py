#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     """ Approach 1: Brute Force, O(N) time: O(N), O(1) """
    #     for num in arr:
    #         if num <= k:
    #             k += 1
    #         elif num > k:
    #             break
    #     return k

    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     """ Approach 2: Binary Search, O(logN) time O(log N), O(1) """
    #     left, right = 0, len(arr) - 1
    #     while left <= right:
    #         pivot = (left + right) // 2
    #         # If number of positive integers
    #         # which are missing before arr[pivot]
    #         # is less than k -->
    #         # continue to search on the right.
    #         if arr[pivot] - pivot - 1 < k:
    #             left = pivot + 1
    #         # Otherwise, go left.
    #         else:
    #             right = pivot - 1

    #     # At the end of the loop, left = right + 1,
    #     # and the kth missing is in-between arr[right] and arr[left].
    #     # The number of integers missing before arr[right] is
    #     # arr[right] - right - 1 -->
    #     # the number to return is
    #     # arr[right] + k - (arr[right] - right - 1) = k + left
    #     return left + k
    
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """ practice: Approach 2: Binary Search, O(logN) time O(log N), O(1) """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid - 1
        # print(f'left: {left}, right: {right}')
        return left + k

        
# @lc code=end

