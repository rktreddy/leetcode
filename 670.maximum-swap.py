#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    # def maximumSwap(self, num: int) -> int:
    #     """ Approach 1: Brute Force O(n^2), O(n) """
    #     num_str = str(num)  # Convert num to string for easy manipulation
    #     n = len(num_str)
    #     max_num = num  # Track the maximum number found

    #     # Try all possible swaps
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             num_list = list(
    #                 num_str
    #             )  # Convert the string to list for swapping

    #             num_list[i], num_list[j] = (
    #                 num_list[j],
    #                 num_list[i],
    #             )  # Swap digits at index i and j
    #             temp = int(
    #                 "".join(num_list)
    #             )  # Convert the list back to string and then to integer

    #             max_num = max(
    #                 max_num, temp
    #             )  # Update max_num if the new number is larger

    #     return max_num  # Return the largest number after all possible swaps
    
    # def maximumSwap(self, num: int) -> int:
    #     """ Approach 2: Greedy Two-Pass O(n), O(n) """
    #     num_str = list(str(num))
    #     n = len(num_str)
    #     max_right_index = [0] * n

    #     max_right_index[n - 1] = n - 1
    #     for i in range(n - 2, -1, -1):
    #         max_right_index[i] = (
    #             i
    #             if num_str[i] > num_str[max_right_index[i + 1]]
    #             else max_right_index[i + 1]
    #         )

    #     for i in range(n):
    #         if num_str[i] < num_str[max_right_index[i]]:
    #             num_str[i], num_str[max_right_index[i]] = (
    #                 num_str[max_right_index[i]],
    #                 num_str[i],
    #             )
    #             return int("".join(num_str))

    #     return num
    
    # def maximumSwap(self, num: int) -> int:
    #     """ Approach 3: Suboptimal Greedy O(n), O(n) """
    #     num_str = str(num)
    #     n = len(num_str)
    #     last_seen = [-1] * 10  # Store the last occurrence of each digit

    #     # Record the last occurrence of each digit
    #     for i in range(n):
    #         last_seen[int(num_str[i])] = i

    #     # Traverse the string to find the first digit that can be swapped with a larger one
    #     for i in range(n):
    #         for d in range(9, int(num_str[i]), -1):
    #             if last_seen[d] > i:
    #                 # Perform the swap
    #                 num_str = list(num_str)
    #                 num_str[i], num_str[last_seen[d]] = (
    #                     num_str[last_seen[d]],
    #                     num_str[i],
    #                 )
    #                 num_str = "".join(num_str)

    #                 return int(
    #                     num_str
    #                 )  # Return the new number immediately after the swap

    #     return num  # Return the original number if no swap can maximize it
    
    # def maximumSwap(self, num: int) -> int:
    #     """ Approach 4: Space Optimized Greedy O(n), O(n) """
    #     num_str = list(str(num))
    #     n = len(num_str)
    #     max_digit_index = -1
    #     swap_idx_1 = -1
    #     swap_idx_2 = -1

    #     # Traverse the string from right to left, tracking the max digit and
    #     # potential swap
    #     for i in range(n - 1, -1, -1):
    #         if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
    #             max_digit_index = i  # Update the index of the max digit
    #         elif num_str[i] < num_str[max_digit_index]:
    #             swap_idx_1 = i  # Mark the smaller digit for swapping
    #             swap_idx_2 = (
    #                 max_digit_index  # Mark the larger digit for swapping
    #             )

    #     # Perform the swap if a valid swap is found
    #     if swap_idx_1 != -1 and swap_idx_2 != -1:
    #         num_str[swap_idx_1], num_str[swap_idx_2] = (
    #             num_str[swap_idx_2],
    #             num_str[swap_idx_1],
    #         )

    #     return int(
    #         "".join(num_str)
    #     )  # Return the new number or the original if no
    #     # swap occurred

    # def maximumSwap(self, num: int) -> int:
    #     """ practice: Approach 4: Space Optimized Greedy O(n), O(n) """
    #     num_str = list(str(num))
    #     n = len(num_str)
    #     max_digit_idx = -1
    #     swap_idx_1 = -1
    #     swap_idx_2 = -1

    #     for i in range(n - 1, -1, -1):
    #         if max_digit_idx == -1 or num_str[i] > num_str[max_digit_idx]:
    #             max_digit_idx = i
    #         elif num_str[i] < num_str[max_digit_idx]:
    #             swap_idx_1 = i
    #             swap_idx_2 = max_digit_idx

    #     if swap_idx_1 != -1 and swap_idx_2 != -1:
    #         num_str[swap_idx_1], num_str[swap_idx_2] = num_str[swap_idx_2], num_str[swap_idx_1]

    #     return int("".join(num_str))

    def maximumSwap(self, num: int) -> int:
        """ practice: Approach 4: Space Optimized Greedy O(n), O(n) """
        num_str = list(str(num))
        n = len(num_str)
        max_digit_idx = swap_idx_1 = swap_idx_2 = -1
        for i in range(n - 1, -1, -1):
            if max_digit_idx == -1 or num_str[i] > num_str[max_digit_idx]:
                max_digit_idx = i
            elif num_str[i] < num_str[max_digit_idx]:
                swap_idx_1 = i
                swap_idx_2 = max_digit_idx

        if swap_idx_1 != -1 and swap_idx_2 != -1:
            num_str[swap_idx_1], num_str[swap_idx_2] = num_str[swap_idx_2], num_str[swap_idx_1]

        return int("".join(num_str))


    #  def maximumSwap(self, num: int) -> int:
    #     """ cracking faang: Approach 4: Space Optimized Greedy O(n), O(n) """
    #     if num <= 11:
    #         return num
        
    #     num_as_arr = collections.deque([])

    #     while num:
    #         num_as_arr.appendleft(num % 10)
    #         num //= 10

    #     max_seen = -1
    #     max_seen_at = len(num_as_arr)
    #     i = len(num_as_arr) - 1
    #     while i >= 0:
    #         cur_num = num_as_arr[i]
    #         num_as_arr[i] = (cur_num, max_seen, max_seen_at)
    #         if cur_num > max_seen:
    #             max_seen = cur_num
    #             max_seen_at = i

    #         i -= 1

    #     i = 0
    #     while i < len(num_as_arr):
    #         cur_num, max_to_right, max_seen_at = num_as_arr[i]
    #         if max_to_right > cur_num:
    #             num_as_arr[i], num_as_arr[max_seen_at] = num_as_arr[max_seen_at], num_as_arr[i]

    #             break
    #         i += 1

    #     num = 0
    #     for cur_num, _, _ in num_as_arr:
    #         num = num * 10 + cur_num

    #     return num

    

# @lc code=end

