class Solution:
    def isPalindrome(self, x: int) -> bool:
        list1 = []
        if x>0:
            while x:
                p = x % 10
                list1.append(p)
                x=x//10
                print(list1)
            for i in range(len(list1)):
                if list1[i] != list1[-i-1]:
                    return False
            return True 
        elif x<0:
            return False
        elif x==0:
            return True
            
                    
                
                
            
        