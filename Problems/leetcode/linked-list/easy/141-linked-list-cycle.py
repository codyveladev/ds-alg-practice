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
        while slow != fast:
            if fast is None or fast.next is None: 
                return False
            slow = slow.next 
            fast = fast.next.next 
        #Find where they overlap again and it will be the origin of the loop
        slow = head 
        while slow != fast: 
            slow = slow.next
            fast = fast.next 
        return slow