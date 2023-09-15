class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        # Count the frequency of each element in nums
        counts = Counter(nums)

        # Sort the elements by their frequencies in descending order
        sorted_elements = sorted(counts.keys(), key=lambda x: -counts[x])

        # Return the top k frequent elements
        return sorted_elements[:k]

                    
            
        