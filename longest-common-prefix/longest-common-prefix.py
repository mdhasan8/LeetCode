class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char = ""
        for elem in range(len(strs[0])):
            #print(elem)
            ch = strs[0][elem]
            for val in range(len(strs)):
                
                #print(val)
                
                if len(strs[val]) > elem and (ch != strs[val][elem]):
                    return char
                elif len(strs[val]) <= elem:
                    return char
                    
                    
            char = char + ch
            
        return char
                    