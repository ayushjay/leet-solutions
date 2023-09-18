class Solution:
    def majorityElement(self, nums: List[int]) -> int:  
        count = {}
        res,maxCount = 0, 0

        for i in nums:

            #create hashMap of keys and their occurence
            count[i] = 1 + count.get(i, 0)

            #result is n if occurence of n is greater than maxCount, otherwise result stays same
            res = i if count[i] > maxCount else res
            #update maxCount of hashMap every iteration of loop
            maxCount = max(count[i], maxCount)
        return res
