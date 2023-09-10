# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binList = []

        while head:
            binList.append(head.val)
            head = head.next

        binaryStr = ""
        for i in binList:
            binaryStr += str(i)

        return int(binaryStr,2)

        