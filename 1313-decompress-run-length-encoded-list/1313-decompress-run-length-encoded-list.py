class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            if i % 2 == 0:
                print(i)
                freq = nums[i]
                val = nums[i+1]

                for j in range(freq):
                    print('j',j)
                    ans.append(val)
                    
        return ans
                
        