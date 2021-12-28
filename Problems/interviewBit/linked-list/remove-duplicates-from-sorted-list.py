# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        #If we have a list of 1 return the list
        if A.next is None: 
            return A 
        currNode = A 
        nextNode = A.next 
        while nextNode: 
            if currNode.val == nextNode.val: 
                #Remove the next node
                removeNode = nextNode
                #Point curr node to next's next
                currNode.next = removeNode.next 
                #Move next up one 
                nextNode = nextNode.next 
            else: 
                currNode = currNode.next
                nextNode = nextNode.next 
        return A