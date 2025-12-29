#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #    """ BruBrute Force O(m * n) , O(1) """
    #     speed = 1
    #     while True:
    #         totalTime = 0
    #         for pile in piles:
    #             totalTime += math.ceil(pile / speed)

    #         if totalTime <= h:
    #             return speed
    #         speed += 1
    #     return speed

    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     """ Binary Search O(n log m), O(1), n is num of piles, m is max. piles """
    #     l, r = 1, max(piles)
    #     res = r

    #     while l <= r:
    #         k = (l + r) // 2

    #         totalTime = 0
    #         for p in piles:
    #             totalTime += math.ceil(float(p) / k)
    #         if totalTime <= h:
    #             res = k
    #             r = k - 1
    #         else:
    #             l = k + 1
    #     return res
    
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     """ practice: Binary Search O(n log m), O(1), n is num of piles, m is max. piles """
    #     l, r = 1, max(piles)
    #     res = r
    #     while l <= r:
    #         k = (l + r) // 2
    #         totalTime = 0
    #         for p in piles:
    #             totalTime += math.ceil(float(p)/k)
    #         if totalTime <= h:
    #             res = k
    #             r = k - 1
    #         else:
    #             l = k + 1
    #     return res
    
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     """ chatgpt(cleader): Binary Search O(n log m), O(1), n is num of piles, m is max. piles """
    #     l, r = 1, max(piles)

    #     while l < r:
    #         k = (l + r) // 2
    #         hours = sum((p + k - 1) // k for p in piles)

    #         if hours <= h:
    #             r = k
    #         else:
    #             l = k + 1

    #     return l
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """ practice: (cleader): Binary Search O(n log m), O(1), n is num of piles, m is max. piles """
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            hours = sum((p + k - 1) // k for p in piles)
            if hours <= h:
                r = k
            else:
                l = k + 1
        return l

# @lc code=end

| Feature              | `l <= r`   | `l < r`             |
| -------------------- | ---------- | ------------------- |
| Search type          | General    | Lower / Upper bound |
| Needs `res`          | Yes        | No                  |
| Risk of bugs         | Higher     | Lower               |
| Return value         | `res`      | `l`                 |
| Interview preference | Acceptable | **Preferred**       |


# 4️⃣ When to Use Each
# Use while l < r when:

# Searching minimum valid value

# Predicate is monotonic

# You want clean + safe code

# Use while l <= r when:

# Searching for exact value

# Predicate is not cleanly monotonic

# You explicitly manage res