class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums1)):
            a = nums1[i]
            found_greater = False
            for j in range(len(nums2)):
                if a == nums2[j]:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            arr.append(nums2[k])
                            found_greater = True
                            break
                    if not found_greater:
                        arr.append(-1)
                    break
        return arr
