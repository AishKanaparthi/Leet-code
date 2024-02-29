
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = l + (r - l) // 2
                if arr[m] == target:
                    return True
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return False
