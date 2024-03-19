# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, param_1, param_2):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = param_1
        self.target = param_2
    
        i = 0
        while i < len(self.nums):
            
            j = i+1
            while j < len(self.nums):
                if (self.nums[i] + self.nums[j] == self.target):
                    return (i, j)
                else: j += 1

            i += 1
        return (i, j)


ret = Solution().twoSum([3,3], 6)