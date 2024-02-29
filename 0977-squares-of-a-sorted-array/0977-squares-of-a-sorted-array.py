class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res= [0] * len(nums)
        l=0
        r= len(nums)-1
        
        while l<=r:
            left,right = abs(nums[l]), abs(nums[r])
            if(left>right):
                res[r-l] = nums[l]* nums[l]
                l+=1
            else:
                res[r-l] = nums[r]* nums[r]
                r-=1
        return res
        
        
        
        
        
        
        
        # arr=[]
        # for i in range(len(nums)):
        #     arr.append(nums[i]*nums[i])
        # return sorted(arr)
            
            