class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length  = 1
    def append(self, value):
        new_node = Node(value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        #Empty List
        if self.length == 0: 
            return False
        #List with 1 or more item(s)
        else: 
            temp = self.head
            prev = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value



    def prepend(self, value):
        if self.length == 0: 
            self.append(value)
        
        
    def insert(self, index, value):
        pass
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next


my_linked_list = LinkedList(4)
# my_linked_list.append(1)
# my_linked_list.append(2)
print(my_linked_list.pop())
my_linked_list.print_list()

