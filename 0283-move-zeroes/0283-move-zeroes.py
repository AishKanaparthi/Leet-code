class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l= 0
        
        for r in range(len(nums)):
            if(nums[l] ==0):
                if(nums[r]==0):
                    r+=1
                
                else:
                    nums[l], nums[r]= nums[r],nums[l]
                    l+=1
                    r+=1
            else:
                l+=1
                r+=1
        return nums
        