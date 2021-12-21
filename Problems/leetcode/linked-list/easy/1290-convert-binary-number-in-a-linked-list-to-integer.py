# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # We can account for zero case
        answer = head.val
        while head.next:
            #Formula for binary repersentation
            answer = answer * 2 + head.next.val
            head = head.next
        return answer