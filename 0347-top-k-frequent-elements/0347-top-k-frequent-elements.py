class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq= [[] for i in range(len(nums)+1)]
        arr=[]
        for n in nums:
            count[n] = 1+ count.get(n,0)
            
        for n,c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                arr.append(n)
                if (len(arr)== k):
                    return arr
            
            
        
        
#         arr=[]
#         count = Counter(nums)
#         a = sorted(count.keys() , key = lambda x: -count[x])
    
#         return a[:k]
            
            
        