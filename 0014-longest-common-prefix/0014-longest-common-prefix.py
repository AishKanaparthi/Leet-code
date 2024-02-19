class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f_ar=[]
        res=""
        
        minlenar= [len(s) for s in strs]
        minlen= min(minlenar)
        for i in range(minlen):
            arr= [s[i] for s in strs] 
            if(len(set(arr)) == 1):
                f_ar.append(arr[0])
                res= ''.join(f_ar)
            else: 
                break
        return res
        
        
            