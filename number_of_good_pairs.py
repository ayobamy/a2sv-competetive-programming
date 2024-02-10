from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_len = len(nums)
        for i in range(num_len):
            for j in range(i + 1, num_len):
                if nums[i] == nums[j]:
                    count += 1
        return count

# Tests
# sol = Solution()
# nums = [1, 2, 3, 1, 1, 3]

# result = sol.numIdenticalPairs(nums)
# print(result)
