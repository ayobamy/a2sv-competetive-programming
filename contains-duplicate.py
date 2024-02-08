class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_len = len(nums)
        distinct_len = len(set(nums))

        return num_len != distinct_len
        
