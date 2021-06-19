class Solution:
    def addBinary(self, a: str, b: str) -> str:
        str1 = ""
        carry = 0
        for elem in range(min(len(a),len(b))):
            #print(elem)
            sum1 = int(a[-elem -1]) + int(b[-elem-1]) + carry
            if sum1 == 2:
                str1= "0" + str1
                carry = 1
            elif sum1 == 1:
                str1= "1" + str1
                carry = 0
            elif sum1 == 0:
                str1= "0" + str1
                carry = 0
            elif sum1 == 3:
                str1= "1" + str1
                carry = 1
                
        if len(a) > len(b):
            for elem in range(len(b),len(a)):
                sum1 = int(a[-elem -1]) + carry
                
                if sum1 == 2:
                    str1= "0" + str1
                    carry = 1
                elif sum1 == 1:
                    str1= "1" + str1
                    carry = 0
                elif sum1 == 0:
                    str1= "0" + str1
                    carry = 0
        if len(b) > len(a):
            for elem in range(len(a),len(b)):
                sum1 = int(b[-elem -1]) + carry
                
                if sum1 == 2:
                    str1= "0" + str1
                    carry = 1
                elif sum1 == 1:
                    str1= "1" + str1
                    carry = 0
                elif sum1 == 0:
                    str1= "0" + str1
                    carry = 0
        if carry !=0:
            str1= "1" + str1
        return str1
                
        
            
            
                
                
        
        