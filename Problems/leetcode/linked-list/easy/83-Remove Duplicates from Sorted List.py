# Definition for singly-linked list.
from typing import Optional

#Commented out on leetcode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# O(n) solution where n is the lenght of the list 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Empty Case 
        if not head:
            return head
        #Two pointers
        curr = head 
        after = head.next
        while after: 
            #If we have duplicate, remove it by pointing curr to the after.next node 
            if curr.val == after.val: 
                curr.next = after.next
                #Set the after node to be next 
                after = after.next    
            else:
                #Increment both pointers by one
                curr = after
                after = after.next
        return head
        