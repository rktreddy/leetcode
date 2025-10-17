#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start
import re
class Solution:        
    # chunkIPv4 = "([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
    # patternIPv4 = "^(" + chunkIPv4 + "\\.){3}" + chunkIPv4 + "$"

    # chunkIPv6 = "([0-9a-fA-F]{1,4})"
    # patternIPv6 = "^(" + chunkIPv6 + "\\:){7}" + chunkIPv6 + "$"

    # def validIPAddress(self, IP: str) -> str:
    #     """ Approach 1: Regex O(1), O(1) """
    #     if re.fullmatch(self.patternIPv4, IP):
    #         return "IPv4"
    #     if re.fullmatch(self.patternIPv6, IP):
    #         return "IPv6"
    #     return "Neither"
    
    def validateIPv4(self, IP):
        nums = IP.split(".")
        for x in nums:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            if x[0] == "0" and len(x) != 1:
                return "Neither"
            # 3. only digits are allowed
            if not x.isdigit():
                return "Neither"
            # 4. less than or equal to 255
            if int(x) > 255:
                return "Neither"
        return "IPv4"

    def validateIPv6(self, IP):
        nums = IP.split(":")
        hexdigits = "0123456789abcdefABCDEF"
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexsigits in one chunk
            if len(x) == 0 or len(x) > 4:
                return "Neither"
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            for ch in x:
                if ch not in hexdigits:
                    return "Neither"
        return "IPv6"

    def validIPAddress(self, IP):
        """ Approach 2: Divide and Conquer O(N), O(1) """
        if IP.count(".") == 3:
            return self.validateIPv4(IP)
        elif IP.count(":") == 7:
            return self.validateIPv6(IP)
        else:
            return "Neither"
        
# @lc code=end

