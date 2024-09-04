# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) despite two loops

        cur = head
        # while cur is not null
        while cur:
            # cur.next is not null and values match
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
                # update for inner loop
            cur = cur.next
        return head
