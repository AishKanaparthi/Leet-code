class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr=[[]]
        
        for num in nums:
            new_subsets=[]
            for subset in arr:
                new_subset = subset +[num]
                new_subsets.append(new_subset)
            arr.extend(new_subsets)
        return arr
            
        