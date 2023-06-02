class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        count = 0
        for val in range(len(seats)):
            count += abs(seats[val] - students[val])

        return count
            
                
        