'''
Problem: 
Merge two sorted linked lists and return it as a new list. 

The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
'''
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
         ans = ListNode(0)
         curr = ans
         first = A
         second = B
         while first is not None and second is not None: 
             if first.val <= second.val: 
                nodeToAdd = ListNode(first.val)
                curr.next = nodeToAdd
                curr = curr.next 
                first = first.next 
             else: 
                nodeToAdd = ListNode(second.val) 
                curr.next = nodeToAdd
                curr = curr.next 
                second = second.next 
         while first is not None: 
            nodeToAdd = ListNode(first.val)
            curr.next = nodeToAdd
            curr = curr.next 
            first = first.next
         while second is not None: 
            nodeToAdd = ListNode(second.val) 
            curr.next = nodeToAdd
            curr = curr.next 
            second = second.next 
         return ans.next