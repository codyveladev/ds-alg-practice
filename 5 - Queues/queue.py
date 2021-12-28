class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue: 
    def __init__(self, value): 
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def enqueue(self, value): 
        new_node = Node(value)
        if self.first is None: 
            self.first = new_node
            self.last = new_node
        else: 
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return 
    
    def dequeue(self): 
        if self.length == 0: 
            return None 
        temp = self.first 
        if self.length == 1: 
            self.first = None 
            self.last = None 
        else: 
            self.first = temp.next 
            temp.next = None 
        self.length -= 1
        return temp 
    
    def print_queue(self): 
        temp = self.first 
        while temp is not None: 
            if temp.next is None: 
                print(temp.value, end="\n")
            else: 
                print(temp.value, end="->")
            temp = temp.next
        return
    

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()