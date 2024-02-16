from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr_len = len(nums)

        expected_sum = arr_len * (arr_len + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum

# Tests
# sol = Solution()
# print(sol.missingNumber([1]))
