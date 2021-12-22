# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	# Have two pointers 
	# 1. Current Node 
	# 2. Next Node 
	# Check if the current node is equal to the next node (Loop)
	# While curr.value = next.value 
	# - If the node is equal, point curr.next to next.next
	curr_node = linkedList
	next_node = linkedList.next
	while next_node: 
		if curr_node.value == next_node.value: 
			#Node to remove is the next node
			remove_node = next_node
			#Current node next is remove_node.next
			curr_node.next = remove_node.next
			#new next node is the next_node.next 
			next_node = next_node.next
		else: 
			#Move the pointers up one increment in the list
			curr_node = next_node
			next_node = next_node.next
	return linkedList