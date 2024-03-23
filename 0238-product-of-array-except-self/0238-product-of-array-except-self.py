class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res= [1]* len(nums)
        res2=[1]* len(nums)
        
        c=1
        d=1
        for i in range(len(nums)):
            res[i] = c
            c*=nums[i]
        for i in range(len(nums)-1, -1, -1):
            res2[i] = d
            d*= nums[i]
        for i in range(len(res)):
            res[i]*= res2[i]
        return res
        
        