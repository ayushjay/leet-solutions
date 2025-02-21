class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T O(n), M O(n)

        if not head:
            return None  # Base case: if the list is empty, return None
        
        newHead = head  # Assume head is the new head initially
        if head.next:  # If there's more than one node in the list
            newHead = self.reverseList(head.next)  # Recursively reverse the rest of the list
            head.next.next = head  # Make the next node's next point back to the current node
        head.next = None  # Set the current node's next pointer to None (to avoid cycle)

        return newHead  # Return the new head of the reversed list

    

# MAGIC HAPPENS HERE:
# head.next.next = head  # Make the next node's next point back to the current node
# Basically , we make the next pointer of head's next node, POINT TO THE HEAD.
"""
Dry Run Example
Let's take an example linked list:

rust
Copy
Edit
1 -> 2 -> 3 -> 4 -> 5 -> None
Recursive Breakdown:
reverseList(1)

Calls reverseList(2)
reverseList(2)

Calls reverseList(3)
reverseList(3)

Calls reverseList(4)
reverseList(4)

Calls reverseList(5)
reverseList(5)

Base case: head.next is None, return 5 (this becomes newHead)
Reversing the Links:
Now we return back up the recursion stack:

head = 4

head.next = 5
5.next = 4 (reverse the link)
4.next = None
Return newHead = 5
head = 3

head.next = 4
4.next = 3
3.next = None
Return newHead = 5
head = 2

head.next = 3
3.next = 2
2.next = None
Return newHead = 5
head = 1

head.next = 2
2.next = 1
1.next = None
Return newHead = 5
Final Reversed List:
rust
Copy
Edit
5 -> 4 -> 3 -> 2 -> 1 -> None
"""
