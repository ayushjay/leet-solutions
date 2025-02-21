from collections import Counter
class Solution:
     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
          
          res = len(students)
          cntMap = Counter()

          # here order of sandwiches is important, we go in order of sandwiches  
          for i in sandwiches:
               if cntMap[i] > 0:
                    res -= 1
                    cntMap -= 1
               else:
                return res
          return res 
     
"""

students = [1,1,1,0]

sandwiches = [1,1,1,0]

count = Counter(students)
print(count) looks like ##  Counter({1: 3, 0: 1})
"""
 