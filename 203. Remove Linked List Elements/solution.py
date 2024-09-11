# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""Used two pointers"""


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        # HERE, prev is dummy
        prev, curr = dummy, head

        while curr:
            nxt = curr.next

            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr

            curr = nxt

        return dummy.next
