class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for val in range(len(jewels)):
            for val2 in range(len(stones)):
                if jewels[val] == stones[val2]:
                    count += 1
        return count
        