class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.strip()
        x= s.split(' ')
        if x:
            return len(x[-1])
        else:
            return 0
        