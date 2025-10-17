#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression


# @lc code=start
class Solution:
#     def compress(self, chars: List[str]) -> int:
#         """ leetcode O(n), O(1) """
#         i = 0
#         res = 0
#         while i < len(chars):
#             group_length = 1
#             while (i + group_length < len(chars)
#                    and chars[i + group_length] == chars[i]):
#                 group_length += 1
#             chars[res] = chars[i]
#             res += 1
#             if group_length > 1:
#                 str_repr = str(group_length)
#                 chars[res:res+len(str_repr)] = list(str_repr)
#                 res += len(str_repr)
#             i += group_length
#         return res
        
    def compress(self, chars: List[str]) -> int:
        """ algomonster O(n), O(1) """
        # Start pointers at the beginning of the list
        read, write, length = 0, 0, len(chars)

        # Process the entire character list
        while read < length:
            # Move read pointer to end of current character sequence
            read_next = read + 1
            while read_next < length and chars[read_next] == chars[read]:
                read_next += 1

            # Write the current character to the write pointer
            chars[write] = chars[read]
            write += 1

            # If we have a sequence longer than 1
            if read_next - read > 1:
                # Convert count to string and write each digit
                count = str(read_next - read)
                for char in count:
                    chars[write] = char
                    write += 1

            # Move read pointer to next new character
            read = read_next

        # Return the length of the compressed list
        return write
# @lc code=end

