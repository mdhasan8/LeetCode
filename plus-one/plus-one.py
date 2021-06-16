class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        var = len(digits)
        flag = False

        for elem in reversed(range(var)):
            print(elem)
            dig = digits[elem]
            dig = dig +1
            if dig == 10:
                flag = True
                digits[elem] = 0
            else:
                flag = False
                digits[elem] = dig
                break
        if flag == True:
            digits.insert(0,1)
        return digits
            
        