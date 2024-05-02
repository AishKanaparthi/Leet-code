class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Sort candidates to easily handle duplicates and maintain consistent order
        candidates.sort()
        
        res = []
        
        def dfs(i, cur, total):
            # If the total is exactly the target, add the current combination to the result
            if total == target:
                res.append(list(cur))
                return
            
            # If total exceeds the target or we reach the end of the candidates list, return
            if total > target or i >= len(candidates):
                return
            
            # Iterate through candidates starting from index 'i'
            for j in range(i, len(candidates)):
                # Skip duplicates to avoid redundant results
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                cur.append(candidates[j])  # Include the current candidate
                dfs(j + 1, cur, total + candidates[j])  # Recurse with the updated total
                cur.pop()  # Backtrack to remove the current candidate
            
        dfs(0, [], 0)  # Start the DFS with an empty combination and total of 0
        
        return res  # Return the list of valid combinations
