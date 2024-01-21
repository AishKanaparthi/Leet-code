class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d_nums1 = set(nums1.copy())
        d_nums2 = set(nums2.copy())
        
        for n in d_nums2.copy():
            if n in d_nums1:
                d_nums1.remove(n)
                d_nums2.remove(n)
                
        return [list(d_nums1), list(d_nums2)]