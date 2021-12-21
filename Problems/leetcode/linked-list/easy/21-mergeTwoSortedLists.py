# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        firstPtr, secondPtr = list1, list2
        #New list to add node onto
        new_list = ListNode(0)
        current_node = new_list
        
        while firstPtr is not None and secondPtr is not None: 
            #Use first ptr
            if firstPtr.val < secondPtr.val: 
                current_node.next = firstPtr
                firstPtr = firstPtr.next 
            #use second ptr
            else: 
                current_node.next = secondPtr
                secondPtr = secondPtr.next 
            
            current_node = current_node.next
    
        #traverse though list if not null
        if secondPtr != None: 
            current_node.next = secondPtr
            secondPtr = secondPtr.next 
        
        #traverse though list if not null
        if firstPtr != None: 
            current_node.next = firstPtr
            firstPtr = firstPtr.next 
        
        
        
        return new_list.next