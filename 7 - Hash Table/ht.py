class HashTable: 
    def __init__(self, size = 7): 
        self.data_map = [None] * size
        return
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value): 
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        return 
    
    def get_item(self, key): 
        index = self.__hash(key)
        if self.data_map[index] is not None: 
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self): 
        keys = []
        for i in range(len(self.data_map)): 
            if self.data_map[i] is not None: 
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys
    
    def values(self):
        values = []
        for i in range(len(self.data_map)): 
            if self.data_map[i] is not None: 
                for j in range(len(self.data_map[i])):
                    values.append(self.data_map[i][j][1])
        return values

    
    def print_table(self): 
        for i, val in enumerate(self.data_map):
            print(i, " : ", val )

my_ht = HashTable()
my_ht.set_item("Apple", 1400)
my_ht.set_item("Test", 120)
my_ht.set_item("Okay", 100)
my_ht.set_item("Tester", 180)
my_ht.set_item("Keyed", 109)
my_ht.print_table()
print(my_ht.get_item("Test"))
print(my_ht.get_item("Orange"))
print(my_ht.keys())
print(my_ht.values())