class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # used two pointers, which are indexes startinmg from index 1,
        # first unique value will be in first position!
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
