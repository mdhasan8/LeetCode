class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: x[-1], reverse=True)
        print(boxTypes)
        count = 0
        ct = 0
        for i in boxTypes:
            print(i[0], i[1])
            ct += i[0]
            print('ct', ct)
            if ct <= truckSize:
                count += (i[0] * i[1])
                          
            else:                
                lt = ct - truckSize 
                print('lt', lt)
                count += i[1] * (i[0] - lt)
                break
        return count
        
        