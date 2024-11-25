class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # create hashmap of both. Use python get, which returns second parameter if no
        # key found
        # we do this to avoid error of not finding the key in first iter
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # python supports dict in equality operator
        return countS == countT
