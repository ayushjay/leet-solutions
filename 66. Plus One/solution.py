class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        one, i = 1, 0

        while one:
            if i < len(digits):
                # 9 at end
                if digits[i] == 9:
                    digits[i] = 0
                # not 9, exit because one is 0
                else:
                    digits[i] += 1
                    one = 0
            # add 1 in end
            else:
                digits.append(1)
                # exit because one is 0
                one = 0
            # increment i
            i += 1
        return digits[::-1]
