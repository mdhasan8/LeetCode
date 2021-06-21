class Solution:
    def mySqrt(self, x: int) -> int:
        
        for elem in range(x+1):
            if elem*elem > x:
                elem = elem - 1
                return elem
        if x == 0:
            return 0
        if x ==1:
            return 1
            
        