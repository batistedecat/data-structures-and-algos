#alles volgens hoorcollege Frederik Gailly
#3e Bachelor Handelsingenieur, Ugent
#door Batiste Decat

class Node():
    def __init__(self, data):
        self.next = None
        self.data = data
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    #accessors
    def print_walk(self):
        curr = self.head
        while curr and curr.next is not None:
            print(curr.data)
            curr = curr.next
    #mutators
    def add_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1
    def add_last_no_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        self.tail = node
        self.size += 1
    def add_last_with_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1