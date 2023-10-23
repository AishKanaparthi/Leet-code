class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            arr.append(nums[i]*nums[i])
        return sorted(arr)
            
            