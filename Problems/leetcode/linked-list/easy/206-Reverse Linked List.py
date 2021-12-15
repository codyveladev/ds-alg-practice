# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None 
        current = head 
        prev = None 
        while current: 
            #Hold the next 
            next = current.next 
            #Set the next node back to prev
            current.next = prev
            #Move prev up one increment 
            prev = current
            #Move current up one increment 
            current = next
        return prev