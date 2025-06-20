class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes 
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        # head (-1) <--> tail (-1)
    
    # This method inserts a new node at the front of the list (right after the dummy head node).
    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    # This method inserts a new node at the end of the list (right before the dummy tail node).
    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    # note how we purposely avoid the dummy head and tail
    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next
        print()


"""
dll = LinkedList()

dll.insertFront(10)  # List: [10]
dll.insertFront(20)  # List: [20, 10]
dll.insertEnd(30)    # List: [20, 10, 30]
dll.insertEnd(40)    # List: [20, 10, 30, 40]
# This results in a list that can be traversed in both directions, starting from dll.head.next (first node) to dll.tail.prev (last node).

 Purpose of Dummy Nodes:
Dummy head and dummy tail are not part of the actual data.

They are helpers to make operations like insert and delete easier.

You never store real values in them (just -1 as placeholder).

Visual Structure After Initialization:

head (-1) <--> tail (-1)
So:

head.next points to tail

tail.prev points back to head

This gives you an empty doubly linked list sandwiched between two dummy nodes.
"""