class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Two pointer problem 
def findLoop(head):
    # Write your code here.
	slow = head.next 
	fast = head.next.next
	#We find where the nodes overlap
	while slow != fast: 
		slow = slow.next
		fast = fast.next.next 
	#Set the slow pointer to the head
	slow = head
	#They will overlap at the origin 
	while slow != fast: 
		slow = slow.next 
		fast = fast.next 
	return fast