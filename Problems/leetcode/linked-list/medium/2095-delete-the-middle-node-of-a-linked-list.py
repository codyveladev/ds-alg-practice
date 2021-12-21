# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0 
        curr = head 
        #Find the length 
        while curr: 
            curr = curr.next 
            length += 1 
        #If we have one or empty list just return head.next for none
        if length <= 1: 
            return head.next
        #Get middle index 
        middle = length // 2 
        #find the middle 
        find = head 
        for _ in range(middle - 1): 
            find = find.next
        #Once found the node to remove will be find.next since we go one before in the loop
        find.next = find.next.next 
        return head