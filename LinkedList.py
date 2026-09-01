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
    def __init__(self, head = None):
        self.head = head
        self.size = 0
    def search(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return curr
            curr = curr.get_next()
        return None
    def length(self):
        return self.size
    #mutators
    def add(self, new_data): #few steps. still need for onother add??
        new_node = Node(new_data, next = self.head)
        if self.head is not None:
            self.head.set_prev(new_node)
        self.head = new_node
        self.size += 1

    def remove(self, data):
        curr = self.root
        while curr:
            if curr.get_data() = data:
                next = curr.get_next()
                prev = curr.get_prev()

                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
                else: #then the this node is the head of the chain, use its next node as new head
                    self.head = next
                self.size -= 1
                return True #succesful deletion
            else:
                curr = curr.get_next()
        return False #if no such node is found


    def __str__(self):
        curr = []
        this_node = self.head
        for i in range(self.size):
            curr.append(this_node.data)
            this_node = this_node.next
        return ', '.join(curr)

