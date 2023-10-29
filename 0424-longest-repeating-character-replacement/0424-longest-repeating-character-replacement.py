class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res=0
        l= 0
        
        count ={}
        win_len=0
         
        
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            f_c= max(count.values())
            win_len= r-l+1
            if(win_len - f_c > k):
                count[s[l]]-=1
                l+=1
            
            res=max(res,r-l+1)
        return res
            