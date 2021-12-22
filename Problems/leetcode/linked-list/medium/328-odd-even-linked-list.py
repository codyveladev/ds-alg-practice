from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = head 
        prev = None
        second = head
        index = 0 
        #set the second pointer to the tail 
        while second.next: 
            second = second.next 
        initialTail = second
        #we have the tail now 
        #we can loop through with the first pointer
        #if we come across and index of odd, append to end 
        #after append set second to the new tail 
        while first != initialTail.next: 
            #Check for odd index 
            if index % 2 != 0: 
                #append new node to end of list
                new_node = ListNode(first.val)
                second.next = new_node
                second = new_node
                #remove connect
                prev.next = first.next
            #Increment pointers
            prev = first
            first = first.next
            index += 1
        return head