from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if (m - 1 < 0 or nums[m - 1] != nums[m]) and (m + 1 >= len(nums) or nums[m + 1] != nums[m]):
                return nums[m]
            else:
                a = m - 1 if nums[m] == nums[m - 1] else m

                if (a % 2):
                    r = m - 1
                else:
                    l = m + 1
