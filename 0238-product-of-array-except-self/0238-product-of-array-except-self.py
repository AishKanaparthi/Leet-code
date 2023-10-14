class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c=1
        d=1
        result =[1]* (len(nums))
        for i in range(len(nums)):
            result[i] = c
            c *= nums[i]
        for j in range(len(nums)-1 , -1, -1):
            result[j] *= d
            d *= nums[j]
        return result
                  
        
        