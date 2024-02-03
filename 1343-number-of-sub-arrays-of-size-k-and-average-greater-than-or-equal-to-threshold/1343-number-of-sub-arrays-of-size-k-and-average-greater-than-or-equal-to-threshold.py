from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarr_count = 0
        current_sum = sum(arr[:k])

        for i in range(k, len(arr)):
            average_val = current_sum / k

            if average_val >= threshold:
                subarr_count += 1

            current_sum += arr[i] - arr[i - k]

        # Check the last subarray after the loop ends
        if current_sum / k >= threshold:
            subarr_count += 1

        return subarr_count
