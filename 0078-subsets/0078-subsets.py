class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
            
            
        
#         arr=[[]]
        
#         for num in nums:
#             new_subsets=[]
#             for subset in arr:
#                 new_subset = subset +[num]
#                 new_subsets.append(new_subset)
#             arr.extend(new_subsets)
#         return arr
            
        