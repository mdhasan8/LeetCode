class Solution:
    def isValid(self, s: str) -> bool:
        
        from queue import LifoQueue
        stk = LifoQueue()
        for elem in range(len(s)):
            elment = s[elem]
            if s[elem] == "(":
                stk.put(s[elem])
            elif s[elem] == ")":
                
                if not stk.empty() and stk.get() == "(":
                    continue
                else: return False
                
            if s[elem] == "{":
                stk.put(s[elem])
            elif s[elem] == "}":
                
                if  not stk.empty() and stk.get() == "{":
                    continue
                else: return False
                
            if s[elem] == "[":
                stk.put(s[elem])
            elif s[elem] == "]":
                
                if  not stk.empty() and stk.get() == "[":
                    continue
                else: return False
        if stk.empty():
            return True
        else: 
            return False
        return True
    
                
    