# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Two Pointers Problem 
	first = head 
	second = head
	counter = 1
	#traverse the second node k times 
	#after traversal check if we are at tail 
	#if so remove first 
	#set first to second position 
	#repeat 	
	while counter <= k: 
		second = second.next 
		counter += 1 
	if second is None: 
		#Remove head 
		head.value = head.next.value
		head.next = head.next.next
		return 
	#Pointing to the node before the end 
	while second.next is not None: 
		second = second.next
		first = first.next
	first.next = first.next.next 
	