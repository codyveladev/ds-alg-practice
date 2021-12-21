# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Return the result.next
	result = LinkedList(0)
	currNode = result 
	firstPtr = linkedListOne 
	secondPtr = linkedListTwo 
	carry = 0
	
	while firstPtr is not None or secondPtr is not None or carry != 0: 
		#If it is none we can just set it to be zero 
		valOne = firstPtr.value if firstPtr is not None else 0
		valTwo = secondPtr.value if secondPtr is not None else 0
		#Add the sum, we can add carry regardless bc if we dont it'll be zero
		sumOfVals = (valOne + valTwo) + carry 
		#Mod to get the remainder to add
		numToAdd = sumOfVals % 10 
		#Divide to get the carry
		carry = sumOfVals // 10 
		#Add new node to the list
		newNode = LinkedList(numToAdd)
		currNode.next = newNode 
		currNode = currNode.next 
		
		#Increment the pointers to next node
		firstPtr = firstPtr.next if firstPtr is not None else None 
		secondPtr = secondPtr.next if secondPtr is not None else None
		
	return result.next