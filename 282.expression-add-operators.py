#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
class Solution:
    # def addOperators(self, num: str, target: int) -> List[str]:
    #     """ Approach 1: Backtracking O(N 4^N), O(N) """
    #     N = len(num)
    #     answers = []
    #     def recurse(index, prev_operand, current_operand, value, string):

    #         # Done processing all the digits in num
    #         if index == N:

    #             # If the final value == target expected AND
    #             # no operand is left unprocessed
    #             if value == target and current_operand == 0:
    #                 answers.append("".join(string[1:]))
    #             return

    #         # Extending the current operand by one digit
    #         current_operand = current_operand*10 + int(num[index])
    #         str_op = str(current_operand)

    #         # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
    #         # valid operand. Hence this check
    #         if current_operand > 0:

    #             # NO OP recursion
    #             recurse(index + 1, prev_operand, current_operand, value, string)

    #         # ADDITION
    #         string.append('+'); string.append(str_op)
    #         recurse(index + 1, current_operand, 0, value + current_operand, string)
    #         string.pop();string.pop()

    #         # Can subtract or multiply only if there are some previous operands
    #         if string:

    #             # SUBTRACTION
    #             string.append('-'); string.append(str_op)
    #             recurse(index + 1, -current_operand, 0, value - current_operand, string)
    #             string.pop();string.pop()

    #             # MULTIPLICATION
    #             string.append('*'); string.append(str_op)
    #             recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
    #             string.pop();string.pop()
    #     recurse(0, 0, 0, 0, [])    
    #     return answers
    
    def addOperators(self, num: str, target: int) -> List[str]:
        """ cracking faang: Backtracking DFS O(N 4^N), O(N) """
        res = []

        def dfs(cur_idx, cur_res, cur_sum, prev):
            if cur_idx >= len(num):
                if cur_sum == target:
                    res.append("".join(cur_res))
                return
            else:
                for i in range(cur_idx, len(num)):
                    cur_str = num[cur_idx: i + 1]
                    cur_num = int(cur_str)

                    if not cur_res:
                        dfs(i + 1, [cur_str], cur_num, cur_num)
                    else:
                        dfs(i + 1, cur_res + ["+"] + [cur_str], cur_sum + cur_num, cur_num)
                        dfs(i + 1, cur_res + ["-"] + [cur_str], cur_sum - cur_num, -cur_num)
                        dfs(i + 1, cur_res + ["*"] + [cur_str], cur_sum - prev + cur_num * prev, cur_num * prev)

                    if num[cur_idx] == '0':
                        break

        dfs(0, [], 0, 0)
        
        return res
        
# @lc code=end

