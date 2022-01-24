#Brute Force Solution
#Try 1
#Easy


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                total = nums[i] + nums[j]
                if total == target and i != j:
                    return [i,j]