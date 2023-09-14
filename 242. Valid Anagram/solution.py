class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = sorted([*s])
        tList = sorted([*t])

        if sList == tList:
            return True
        else:
            return False