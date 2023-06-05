class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        app = []
        for val in range(len(names)):
            t1 = (heights[val], names[val])
            app.append(t1)
        app.sort(reverse = True)

        res = []
        for val2 in range(len(app)):
            res.append(app[val2][1])
        return res
        
        
#         my_dict = dict(zip(names, heights))
#         #print(my_dict) 
#         # myvalues = list(my_dict.values())
#         # print(myvalues)
#         # myvalues.sort()
        
#         twolist = [names,heights]
#         print(twolist.sort())
        
#         return my_dict.keys()
        
        
#         ans = []
#         for i in range(len(names)):
#             print(i)
#             if max(heights):
#                 index = heights.index(max(heights))
#                 print(index)
#                 print('heights', heights)
#                 ans.append(names[index])
#                 heights.remove(heights[index])
#                 names.remove(names[index])
#         return ans
    

            
            
#             for j in range(len(heights)):
#                 if heights[i] > heights[j]:
#                     print(heights[i])
#                     print("j", heights[j])
#                     ans.append(names[i])
#                     break
#                 else:
#                     ans.append(names[i])
#                     break
#         return ans
            

