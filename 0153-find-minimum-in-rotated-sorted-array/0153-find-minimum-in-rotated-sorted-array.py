class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        for r in range(1,len(nums)):
            if(nums[r]> nums[r-1]):
                r+=1
            else:
                return nums[r]
        return nums[l]