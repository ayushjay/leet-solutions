class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right = ListNode(), ListNode()
        ltail, rtail = left,right
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next

            head = head.next

        ltail.next = right.next = None
        rtail.next = rtail.next

        return ltail.next