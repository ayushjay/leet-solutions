# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        # fast.next: Ensures that fast.next is not None. If fast.next is None, attempting to access fast.next.next in the next iteration would result in an error.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
