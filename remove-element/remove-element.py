class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for elem in range(len(nums)):
            while elem < len(nums) and nums[elem] == val:
                nums.pop(elem)
                
        