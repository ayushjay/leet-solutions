class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1!= l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
    
    """
    l1, l2 are listnodes. while l1 value != l2 value, while loop runs. 
    l1.next goes till l1 is not null otherwise we assign headB to it.
    Similarly, l2.next goes till we assign headA to it. this will ensure both poiners are moving TOGETHER
    then, when l1==l2, we return l1 (or even l2)

    """