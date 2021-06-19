class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        var1 = -1000000
        var = 0
        for elem in range(len(nums)):
            var = nums[elem] + var
            if var1 < var:
                var1 = var
            if var < 0:
                var = 0
            else:
                var     
        return var1
                
        