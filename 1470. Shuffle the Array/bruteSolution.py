class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            #we do i+n so it can go 0+3 and so on
            
            res.append(nums[i + n])
        return res
