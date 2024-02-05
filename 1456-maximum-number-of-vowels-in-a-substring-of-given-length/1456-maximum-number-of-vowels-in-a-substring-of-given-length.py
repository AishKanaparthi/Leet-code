# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         vowels=["a","e","i","o","u"]
#         char= []
#         arr=[]
#         count=0
#         l=0
#         for r in range(len(s)):
#             count=0
#             if len(char)<=k:
#                 char.append(s[r])
                
#             else:
#                 char.remove(s[l])
#                 l+=1
#                 for i in range(len(char)):
#                     if char[i] in vowels:
#                         count+=1
#                     arr.append(count)
            
            
#         return arr

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        char = []
        arr = []
        count = 0
        l = 0
        max_count = 0
        
        for r in range(len(s)):
            if len(char) < k:
                char.append(s[r])
                if s[r] in vowels:
                    count += 1
            else:
                if s[l] in vowels:
                    count -= 1
                char.remove(s[l])
                l += 1
                
                char.append(s[r])
                if s[r] in vowels:
                    count += 1

            max_count = max(max_count, count)

        return max_count



                
                
            
        