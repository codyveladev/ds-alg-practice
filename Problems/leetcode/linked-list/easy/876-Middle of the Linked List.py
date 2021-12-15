# Definition for singly-linked list.
from typing import Optional
#This is commented out on the leetcode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#O(n) solution where N is the length of the list  
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.get_length(head)
        mid = length // 2
        middle_node = self.find_by_index(head, mid)
        return middle_node
    
    def get_length(self, head):
        temp = head
        count = 0
        while temp: 
            temp = temp.next
            count += 1 
        return count 
    
    def find_by_index(self, head ,index):
        temp = head 
        for _ in range(index):
            temp = temp.next 
        return temp