from functools import lru_cache
"""Caculator max some of elements in list without two adjacent elements"""

class Solution:
    def rob(self, A):
        @lru_cache
        def rob(i):
            if i >= len(A):
                return 0
            return max(rob(i+1), A[i] + rob(i+2))
        return rob(0)

test_case = [2,7,9,3,1]

solution = Solution()

print(solution.rob(test_case))

