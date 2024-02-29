class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        arr1=[]
        arr2=[]
        for i in range(len(nums)):
            if(nums[i]<0):
                arr1.append(nums[i])
            elif(nums[i]>0):
                arr2.append(nums[i])
        return max(len(arr1),len(arr2))
        
        
        