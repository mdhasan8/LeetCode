class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        a = nums[0]
        b = nums[1]
        c = nums[-1]
        d = nums[-2]
        
        return (c * d) - (a * b)