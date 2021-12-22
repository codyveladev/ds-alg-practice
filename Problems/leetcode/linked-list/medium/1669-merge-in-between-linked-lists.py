# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        #Get the prev 
        #Because we want to set this to the head of next list
        firstNode = self.findNodeByIndex(list1, a - 1)
        #Get the node position 
        #We want to set the tail of list two to the next of this node 
        secondNode = self.findNodeByIndex(list1, b)

        #Set the firstNode's next to head of the other list
        headOfSecondList = list2 
        firstNode.next = headOfSecondList 
        #Traverse to second list's tail 
        tailOfSecondList = headOfSecondList
        while tailOfSecondList.next is not None: 
            tailOfSecondList = tailOfSecondList.next
        #Set the tail of the next node to 
        tailOfSecondList.next = secondNode.next
        
        return list1   
    
    #Helper function O(n)
    def findNodeByIndex(self, llist, index):
        nodeToFind = llist
        for _ in range(index): 
            nodeToFind = nodeToFind.next
        return nodeToFind