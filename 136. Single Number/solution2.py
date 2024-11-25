class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashSet = set()

        for i in nums:
            if i not in hashSet:
                hashSet.add(i)
            else:
                hashSet.remove(i)
        return hashSet.pop()