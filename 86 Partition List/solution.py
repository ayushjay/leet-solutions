class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """these are dummy list nodes, NOT LINKED LISTS"""
        left,right = ListNode(), ListNode() 
        #here we are choosing this to point since left, rgiht are DUMMY nodes
        ltail, rtail = left,right


        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next

            head = head.next

        ltail.next = right.next 
        rtail.next = None
        return left.next