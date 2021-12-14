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
            # Handle if the list only had one element
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else:
            #Store the current head
            prev_head = self.head
            #Make the new value the head
            self.head = new_node
            #Make the next value the previous head
            self.head.next = prev_head
        self.length += 1
        return True
    
    def pop_first(self): 
        if self.length == 0: 
            return False
        else:
            # Prev head
            old_head = self.head 
            self.head = old_head.next
            old_head.next = None
            self.length -= 1
            if self.length == 0: 
                self.tail = None
            return old_head
    
    def get(self, index): 
        if index >= self.length or index < 0: 
            return None
        temp = self.head 
        for _ in range(index): 
            temp = temp.next
        return temp
    
    def set_val(self, index, value):
        temp = self.get(index)
        if temp: 
            temp.value = value
            return True
        return False 
        
            
    def insert(self, index, value):
        #Check for valid index
        if index >= self.length or index < 0: 
            return None
        #Set new node
        new_node = Node(value)
        #Node currently at index to insert
        insert_node = self.get(index)
        #Node before index to insert
        prev_node = self.get(index - 1)
        #If the index is 0, insert value at top of list
        if index == 0: 
            self.prepend(value)
        else: 
            #Prev node point to new node
            prev_node.next = new_node
            #New node point to insert node
            new_node.next = insert_node
            #Increment length by 1 
            self.length += 1
        return True
    
    def remove(self, index): 
        if self.length == 0: 
            return None
        #If the prev node does not exist we are at the front of the list
        if index == 0: 
            self.pop_first()
            return True
        #If we want to remove the last item in the list, use pop 
        if index == self.length - 1: 
            self.pop()
            return True
        #Previous node
        prev_node = self.get(index - 1)
        node_to_remove = prev_node.next
        #prev node point to the next node
        prev_node.next = node_to_remove.next
        #Node to remove points to nothing
        node_to_remove.next = None
        self.length -= 1
        return node_to_remove
    
    def reverse(self): 
        # Switch head and tail 
        temp = self.head 
        self.head = self.tail 
        #Set pointers 
        after = temp.next
        before = None
        while temp: 
            #Move the after var along
            after = temp.next
            #Move the arrow around 
            temp.next = before 
            #Change the node into the curr
            before = temp 
            #Set the curr node to the node next in the list
            temp = after
            

    

    def print_list(self):
        temp = self.head
        while temp:
            if temp.next is None: 
                print(temp.value, end= "->None \n")
            else: 
                print(temp.value, end="->")
            temp = temp.next


my_linked_list = LinkedList(4)
my_linked_list.append(42)
my_linked_list.append(18)
# print(my_linked_list.pop())

my_linked_list.prepend(10)



my_linked_list.print_list()
print("Get: ", my_linked_list.get(1))

my_linked_list.pop_first()
my_linked_list.set_val(2, 1100)
my_linked_list.insert(2, 90)

my_linked_list.print_list()

my_linked_list.remove(3)
my_linked_list.print_list()

my_linked_list.reverse()
my_linked_list.print_list()

