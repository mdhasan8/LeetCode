class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        count = 0
        for elem in operations:
            if elem == '--X':
                count -= 1
            elif elem == 'X--':
                count -= 1
            elif elem == '++X':
                count += 1
            elif elem == 'X++':
                count += 1
        return count
        