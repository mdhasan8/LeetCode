class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sm = 0
        
        for i in range(len(nums)):
            
            if i % 2 == 0:
                ev = nums[i]
                od = nums[i+1]
                tup = (ev,od)
                sm += min(tup)
        return sm
            
                
                
        