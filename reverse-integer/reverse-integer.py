class Solution(object):
    def reverse(self, x):
        mx=2147483647
        mn=-2147483648
        re=0
        negativeFlag = False
        if (x < 0):
     
            negativeFlag = True
            x = -x
        
        while x:
            re=re*10
            re+=x%10
            x=x/10
            
        if (negativeFlag == True):
            re =-re
        else:
            re
        if(re>mx or re<mn):
            re=0
        return re 
        