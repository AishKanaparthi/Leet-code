class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        res=0
        total = float('inf')  
        for r in range(len(nums)):
            res=res+ nums[r]
            
            while res>= target:
                total = min(total, r-l+1)
                res= res- nums[l]
                l+=1
            
        return total if total!= float('inf') else 0
                
                
        