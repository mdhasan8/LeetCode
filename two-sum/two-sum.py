class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            val1 = nums[x] 
            for y in range(x+1,len(nums)):
                val2 = nums[y]
                if (x!=y and val1+val2 == target):
                    return x,y
                    
        