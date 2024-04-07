class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res1= [[1] for i in range(len(nums))]
        res2 = [[1] for i in range(len(nums))]
        final_res = []
        c=1
        d=1
        
        for i in range(len(nums)):
            res1[i] =c
            c *=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res2[i] = d
            d *= nums[i]
        for i in range(len(res1)):
            final_res.append(res1[i]* res2[i])
        
            
        
        
            
        return final_res
               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res= [1]* len(nums)
#         res2=[1]* len(nums)
        
#         c=1
#         d=1
#         for i in range(len(nums)):
#             res[i] = c
#             c*=nums[i]
#         for i in range(len(nums)-1, -1, -1):
#             res2[i] = d
#             d*= nums[i]
#         for i in range(len(res)):
#             res[i]*= res2[i]
#         return res
        
        