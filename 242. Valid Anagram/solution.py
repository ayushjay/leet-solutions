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
        # to avoid error in which "c" key is not found in countT, we use python get
        # very importantly, python GET() compares the values for THAT PARTICULAR value
        # example for 'ab' and 'ba', {"a":1,"b":1} & {"b":1, "a":1}, so it WILL compare THAT VALUE a or b itself
        # using python get()
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
