# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
         #Here we write both fast and fast.next since FAST.NEXT is next iteration and FAST is moving twice as slow 
        """
        The condition while fast and fast.next ensures that you can safely access fast.next without encountering a NoneType error. 
        If fast becomes None, it means that you've reached the end of the linked list, and there is no cycle.
        Similarly, if fast.next becomes None, it means that you've reached the end of the list one step ahead of slow, which also indicates there is no cycle.
        """
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
