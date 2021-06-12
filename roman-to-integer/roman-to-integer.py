class Solution:
    def romanToInt(self, s: str) -> int:
        I = 1  
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        var = 0
        
        for ele in range(len(s)):
            value = s[ele]
            print(value)
            if s[ele]=="I":
                if ele+1 < len(s) and (s[ele+1] == "V" or s[ele+1] == "X"):
                    var = var -1
                else:
                    var = var +1
            if s[ele]=="V":
                var = var +5
            if s[ele]=="X":
                if ele+1 < len(s) and (s[ele+1] == "L" or s[ele+1] == "C"):
                    var = var -10
                else:
                    var = var +10
            if s[ele]=="L":
                var = var +50
            if s[ele]=="C":
                if ele+1 < len(s) and (s[ele+1] == "D" or s[ele+1] == "M"):
                    var = var -100
                else:
                    var = var +100
            if s[ele]=="D":
                var = var +500
            if s[ele]=="M":
                
                var = var +1000
            
        return var         
        
        
        