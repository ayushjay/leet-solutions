#list1, list are heads

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

          #compare both till both are non NULL
        while list1 and list2:
            if list1.val < list2.val:
                
                tail.next = list1
                

   
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
        
        return dummy.next  
    