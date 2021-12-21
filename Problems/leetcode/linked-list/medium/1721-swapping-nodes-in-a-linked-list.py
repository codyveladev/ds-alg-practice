# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next: 
            return head      
        firstNode = self.findKFromHead(head, k)
        secondNode = self.findKFromTail(head, k)
        #Swap vals 
        temp = firstNode.val
        firstNode.val = secondNode.val
        secondNode.val = temp
        return head 
    
    def findKFromHead(self, head, k):
        kFromHead = head 
        for _ in range(k - 1): 
            kFromHead = kFromHead.next 
        return kFromHead
    
    def findKFromTail(self, head, k): 
        counter = 1
        firstPtr = head 
        secondPtr = head
        #Set the second ptr k away from first
        while counter <= k: 
            secondPtr = secondPtr.next 
            counter += 1
        #If we reach the tail head is k away
        if secondPtr is None: 
            return firstPtr 
        #Traverse to the end of the list 
        while secondPtr: 
            secondPtr = secondPtr.next 
            firstPtr = firstPtr.next
        #K away from the tail
        return firstPtr   