class Solution:
    def minimumSum(self, num: int) -> int:
        
        r = []

        while num:
            r.append(num % 10)
            num = num //10
            
        r.sort()

        return r[0] * 10+ r[2] + r[1] * 10 + r[3] 
