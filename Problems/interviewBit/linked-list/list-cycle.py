# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A.next is None: 
            return None 
        fast = A.next.next
        slow = A.next
        while fast != slow and fast is not None and fast.next is not None: 
            fast = fast.next.next 
            slow = slow.next
        if fast is None or fast.next is None: 
            return None 
        slow = A 
        while fast != slow: 
            slow = slow.next 
            fast = fast.next 
        return slow