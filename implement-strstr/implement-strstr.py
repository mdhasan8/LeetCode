class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """x = len(haystack)
        y = len(needle)
        if y==0:
            return 0
        for elem in range(x):
            flag = True
            for val in range(y):
                
                if elem+val >= x or needle[val] != haystack[elem+val]:
                    flag = False
                    break
            if flag == True:
                return elem
        
        return -1"""
        if needle == "":
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        