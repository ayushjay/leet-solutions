from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = 0
        numsSet = set(nums)
        print(numsSet)

        if len(numsSet) == len(nums):
            return False
        else:
            return True