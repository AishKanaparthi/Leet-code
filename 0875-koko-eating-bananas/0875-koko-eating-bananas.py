

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        while l <= r:
            m = l + (r - l) // 2
            res = 0
            
            for pile in piles:
                res += (pile + m - 1) // m  # Ceiling division
                
            if res <= h:
                r = m - 1
            else:
                l = m + 1
        
        return l
