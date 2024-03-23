class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d= set(nums)
        
        d= sorted(d)
        a=[[]]
        b=[]
        if d==[]:
            return 0
        for i in range(len(d)-1):
            if(d[i]+1 == d[i+1]):
                b.append(d[i])
            else:
                a.append(b)
                b=[]
                
        a.append(b)
        max_len= max(a, key=len)
                    
        return len(max_len)+1
        