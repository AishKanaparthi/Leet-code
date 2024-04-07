class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        for char in text:
            count[char] = count.get(char, 0) + 1
        
        b_count = count.get('b', 0)
        a_count = count.get('a', 0)
        l_count = count.get('l', 0) // 2  # Since we need two 'l's for each balloon
        o_count = count.get('o', 0) // 2  # Since we need two 'o's for each balloon
        n_count = count.get('n', 0)
        
        return min(b_count, a_count, l_count, o_count, n_count)
