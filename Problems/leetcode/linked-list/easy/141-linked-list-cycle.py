# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None: 
            return False
        slow = head.next 
        fast = head.next.next
        #Find where the nodes overlap each other
        #If they ever equal each other we have a loop
        while fast and fast.next:
            if slow == fast: 
                return True
            else: 
                slow = slow.next
                fast = fast.next.next
        return False