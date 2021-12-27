from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head 
        #Get halfway to the list
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next 
        #Reverse the second half of the list
        slow = self.reverse(slow)
        #Point fast back to the top of the list
        fast = head
        #Traverse the two lists and see if they dont equal each, if true return false
        while slow is not None: 
            if slow.val != fast.val:
                return False
            slow = slow.next 
            fast = fast.next
        #Didnt meet unequal condition so return true 
        return True
    
    #Reverse helper function    
    def reverse(self, head):
        prev = None
        while head is not None: 
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev