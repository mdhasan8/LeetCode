class Solution:
    def sortSentence(self, s: str) -> str:
        res = []
        s = s.split()
        arr = []
        for elem in s:
            arr.append(elem)
        print(arr)
        num = []        
        for val in range(len(arr)):
            num.append((arr[val][-1], arr[val][:-1]))
        num.sort()
                
        res = []
        for val2 in range(len(num)):
            print("num[val2][1]",num[val2][0])
            print(num[0][0])
            res.append(num[val2][1])
        
        return " ".join(res)
        
            
                