# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
		if A.next is None: 
			return 1
		fast = A.next.next
		slow = A.next 
		while fast and fast.next: 
			fast = fast.next.next
			slow = slow.next 
		slow = self.reverseList(slow)
		fast = A 
		while slow and fast: 
			if slow.val != fast.val: 
				return 0
			else: 
				slow = slow.next 
				fast = fast.next 
		return 1
	def reverseList(self, head): 
		curr = head 
		prev = None
		while curr: 
			next_node = curr.next 
			curr.next = prev
			prev = curr
			curr = next_node
		return prev 