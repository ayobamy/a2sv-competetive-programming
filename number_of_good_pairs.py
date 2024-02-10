class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_len = len(nums)
        for i in range(num_len):
            for j in range(i + 1, num_len):
                if nums[i] == nums[j]:
                    count += 1
        return count
