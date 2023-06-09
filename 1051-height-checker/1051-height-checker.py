class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expec = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expec[i]:
                count+=1
        return count
        