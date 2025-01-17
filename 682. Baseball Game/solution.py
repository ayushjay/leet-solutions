class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreArr = []
        for i in operations:
            if i == "+":
                scoreArr.append(scoreArr[-1]+ scoreArr[-2])
            elif i == "D":
                scoreArr.append(scoreArr[-1] * 2)
            elif i == "C":
                scoreArr.pop()
            else:
                scoreArr.append(int(i))

        return sum(scoreArr)
        
        

        