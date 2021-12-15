class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None
        self.prev = None

class DoublyLinkedList: 
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else: 
            #Point curr tail's next to new node 
            self.tail.next = new_node
            #Point new node's prev back to curr tail 
            new_node.prev = self.tail
            #Set the tail as the new node 
            self.tail = new_node
        #increment length 
        self.length += 1
        return True
    
    def pop(self): 
        #Empty List
        if self.length == 0: 
            return None
        #List with only one item 
        if self.length == 1: 
                self.head = None
                self.tail = None
                self.length -= 1
                return self.head
        #Multiple items in list
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            return temp
    
    def prepend(self, value): 
        new_node = Node(value)
        #Empty list
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else: 
            # New node next point to curr head 
            new_node.next = self.head
            #curr head prev set to new node 
            self.head.prev = new_node
            #Set the head to the new head 
            self.head = new_node
            #Increment the length by 1 
        self.length += 1
        return self.head
    
    def pop_first(self): 
        #Empty List
        if self.length == 0: 
            return None
        #Old head 
        temp = self.head
        #One item in list
        if self.length == 1: 
            self.head = None 
            self.tail = None
        else: 
            #Set the head to the new head
            self.head = self.head.next 
            #Point the new head's prev to None instead of old head 
            self.head.prev = None 
            #Point old head's next to None 
            temp.next = None 
        self.length -= 1
        return temp.value
    
    def get(self, index): 
        if index < 0 or index >= self.length: 
            return None
        else: 
            temp = self.head 
            mid = self.length // 2
            if mid >= index: 
                for _ in range(index): 
                    temp = temp.next
            else: 
                temp = self.tail 
                for _ in range(self.length - 1, index, 1): 
                    temp = temp.prev
            return temp
    
    def set_val(self, index, value):
        temp = self.get(index)
        if temp: 
            temp.value = value
            return True
        return False

    def insert(self, index, value): 
        if index < 0 or index >= self.length: 
            return None
        if index == 0: 
            return self.prepend(value)
        if index == self.length: 
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        #Set the pointers for before
        before.next = new_node
        new_node.prev = before
        #Set the pointers for after 
        after.prev = new_node
        new_node.next = after
        return True
    
    def remove(self, index): 
        if index < 0 or index >= self.length: 
            return None 
        if index == 0: 
            return self.pop_first()
        if index == self.length - 1: 
            return self.pop()
        node_to_remove = self.get(index)
        before = node_to_remove.prev
        after = node_to_remove.next
        #Set pointers
        before.next = after
        after.prev = before 
        #Remove connections 
        node_to_remove.next = None 
        node_to_remove.prev = None 
        self.length -=1
        return node_to_remove

    def print_list(self):
        temp = self.head
        while temp: 
            if not temp.next: 
                print(temp.value, end=" <--> None \n")
            else: 
                print(temp.value, end=" <--> ")
            temp = temp.next

my_dbl_list = DoublyLinkedList(1)

my_dbl_list.append(2)
my_dbl_list.append(5)

my_dbl_list.prepend(15)
# print(my_dbl_list.set_val(3,8))
my_dbl_list.insert(1, 69)
print(my_dbl_list.remove(2))
my_dbl_list.print_list()
    