class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

          #compare both till both are non NULL
        while list1 and list2:
            if list1.val < list2.val:
                #here l1 since we are adding the listNode, not its value
                tail.next = list1
                #here, we are breaking connections so elements in list1 keep moving forward
                #this is how linkedList works

                """
                The line list1 = list1.next is used to move the list1 pointer forward in the linked list. 
                In a singly linked list, each node has a next attribute pointing to the next node in the list. 
                When you set list1 to list1.next, you are essentially updating the list1 pointer to point to the next node in the list.

Here's what happens step by step:

Initially, list1 points to the current node in list1. Let's call this node A.

When list1 = list1.next is executed, list1 is reassigned to point to the next node in the list, which is the node that follows A.

list1 now points to the next node in the list, which we'll call B.

This process continues as you iterate through the linked list, effectively moving list1 from one node to the next with each iteration of the loop.

By moving the list1 pointer forward, you ensure that you are comparing and processing each node in list1 one by one as you traverse the linked list. 
                """
                list1 = list1.next  # Move list1 pointer forward
            else:
                tail.next = list2
                list2 = list2.next  # Move list2 pointer forward

            tail = tail.next
         #here we are adding REMAINING part of list1 to tail
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
         #return head of dummy node
        return dummy.next  