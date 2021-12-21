# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: 
            return 
        firstPtr = head 
        secondPtr = head 
        firstPtrPrev = None 
        counter = 1
        #Move the second Ptr up for places 
        while counter <= n: 
            secondPtr = secondPtr.next
            counter += 1
        #check if we are at the end 
        if secondPtr is None: 
            #Return list without the head
            return head.next
        else: 
            #We traverse to the end of the list 
            #while keeping the distance from 1st to second 
            while secondPtr is not None:
                firstPtrPrev = firstPtr
                firstPtr = firstPtr.next 
                secondPtr = secondPtr.next 
            #Removal Logic 
            firstPtrPrev.next = firstPtr.next
            return head  