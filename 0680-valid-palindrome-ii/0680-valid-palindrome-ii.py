class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r= len(s) -1
        
        while l<r:
            if(s[l] == s[r]):
                l+=1
                r-=1
            else:
                return self.validPalindromeUtil(s, l + 1, r) or self.validPalindromeUtil(s, l, r - 1)  
        return True
    
    def validPalindromeUtil(self, s: str,l ,r) -> bool:
        
        while l<r:
            if(s[l] == s[r]):
                l+=1
                r-=1
            else:
                return False
        return True
            
            
            
            
            