class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        ind = len(nums)//2
        for val in range(0, ind):
            print(val)
            ans.append(nums[val])
            ans.append(nums[ind]) 
            ind += 1
 
        return ans
        