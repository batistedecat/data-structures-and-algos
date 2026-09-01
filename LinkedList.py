class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    #accessors
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev

    #mutators
    def set_data(self,data):
        self.data = data
    def set_next(self,next):
        self.next = next
    def set_prev(self,prev):
        self.prev = prev

class LinkedList: #Doubly linked
    def __init__(self, r = None, t = None):
        self.head = r
        self.tail = t
        self.size = 0
    #accessors
    def search(self, data):
        pass
    def length(self):
        return self.size
    #mutators


    def Front_add(self, new_data): #few steps. still need for onother add??
        new_node = Node(new_data)
        if self.head:
            self.head.set_prev(new_node)
        self.head = new_node
        self.size += 1
    def Rear_add(self, new_data):
        pass


    def remove(self, data):
        pass


