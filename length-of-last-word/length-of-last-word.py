class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        flag = False
        
        for char in range(len(s)):
            if s[char] == " ":
                flag = True
            
            
            elif flag == False:
                count += 1
            
            else:
                count = 1
                flag = False
            
                
            
            
            
            
        return count        
        