class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []

        
        for elem in range(len(nums)):
            count = 0
            for val in range(len(nums)):
                if nums[elem] > nums[val]:
                    count += 1
            ans.append(count)
        return ans
        