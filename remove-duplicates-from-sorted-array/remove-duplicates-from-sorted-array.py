class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''for elem in range(len(nums)):
            #val = nums[elem]
            if elem + 1 < len(nums) and nums[elem] == nums[elem+1]:
                nums.pop(elem+1)'''
        
        k=0
        for i in range(1,len(nums)):
            if nums[k]!=nums[i]:
                k=k+1
                nums[k]=nums[i]
            
        del nums[k+1:len(nums)]

        
        