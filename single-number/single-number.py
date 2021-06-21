class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for elem in range(len(nums)):
            a = nums[elem] ^ a
        return a
            
        