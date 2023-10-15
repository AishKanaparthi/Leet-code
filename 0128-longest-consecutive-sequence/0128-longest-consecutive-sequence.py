class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=set(nums)
        a= sorted(d)
        
        b=[]
        c=[[]]
        if(a==[]):
            return 0
        else:
            for i in range(len(a)-1):
                if(a[i]+1 == a[i+1]):
                    b.append(a[i])
                else:
                    c.append(b)
                    b=[]
                    
            
            c.append(b)
            max_length = max(c, key=len)
        return len(max_length)+1
        