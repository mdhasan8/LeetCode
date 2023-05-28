class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        count = 0
        for val in range(len(nums1)):
            print("val", nums1[val])

            if nums1[val] == 0 and  count < len(nums2):
                nums1[val] = nums2[count]
                count  += 1
                    
        nums1.sort()                
        print(nums1)


