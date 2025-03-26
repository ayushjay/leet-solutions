# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Base case: if head is None or only one node, return head
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Adjust pointers
        head.next.next = head
        head.next = None
        
        return new_head #Every time, a new_head is being returned, final one is reversed one
 
# -----------------------------------
# DRY RUN FOR INPUT: 1 -> 2 -> 3 -> 4
# -----------------------------------
# reverse_recursive(1)
#   -> head = 1, calls reverse_recursive(2)
# reverse_recursive(2)
#   -> head = 2, calls reverse_recursive(3)
# reverse_recursive(3)
#   -> head = 3, calls reverse_recursive(4)
# reverse_recursive(4)
#   -> head = 4, base case reached, returns 4

# Now we start unwinding:

# Returning from reverse_recursive(3)
#   - head = 3, new_head = 4
#   - 3.next.next = 3  (Making 4 -> 3)
#   - 3.next = None    (Breaking original link)
#   - Returns 4 -> 3 -> None

# Returning from reverse_recursive(2)
#   - head = 2, new_head = 4
#   - 2.next.next = 2  (Making 3 -> 2)
#   - 2.next = None    (Breaking original link)
#   - Returns 4 -> 3 -> 2 -> None

# Returning from reverse_recursive(1)
#   - head = 1, new_head = 4
#   - 1.next.next = 1  (Making 2 -> 1)
#   - 1.next = None    (Breaking original link)
#   - Returns 4 -> 3 -> 2 -> 1 -> None

# FINAL OUTPUT:
# 4 -> 3 -> 2 -> 1 -> None

# When reverse_recursive(4) returns 4, it goes back up to reverse_recursive(3)