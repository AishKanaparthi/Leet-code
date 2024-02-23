class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        
        arr=[]
        while i< len(word1) and j< len(word2):
            arr.append(word1[i])
            arr.append(word2[j])
            i+=1
            j+=1
        if(len(word1)>len(word2)):
            arr.append(word1[i:])
            
        arr.append(word2[j:])
        a= ''.join(arr)
        return a
            
            
        
        