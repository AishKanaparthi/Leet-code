class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #for i, n in enumerate(nums):
         #   if(n== target):
         #       return i
            
        #return -1
        
        l,r= 0, len(nums)-1
        
        while l<=r:
            m = l+ ((r-l)//2)
            if(nums[m]>target):
                r= m-1
            elif(nums[m]<target):
                l=m+1
            else:
                return m
        
        return -1

            
            
        