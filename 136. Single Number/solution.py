class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res = n ^ res
        return res
    

"""for example if nums=[4,1,2,1,2], then bit XOR operations on 4,1,2,1,2 will always return 4 
"""