class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        mx = max(candies)
        print(mx)
        print(extraCandies)
        
        for i in range(len(candies)):
            if (candies[i] + extraCandies) < mx:
                ans.append(False)
            else:
                ans.append(True)
        return ans
        