class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l=m
        r=0
        
        while r < len(nums2):
            nums1[l] = nums2[r]
            l+=1
            r+=1
        nums1.sort()
        return nums1
            
        
        