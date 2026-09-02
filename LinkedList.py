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
        curr = self.head
        while curr:
            if curr.get_data() == data:
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


    def __repr__(self):
        curr = []
        this_node = self.head
        for i in range(self.size):
            curr.append(this_node.data)
            this_node = this_node.next


        return ', '.join(str(x) for x in curr)
    #extra shit
    def sum(self):
        curr = 0
        this_node = self.head
        while this_node is not None:
            d = this_node.get_data()
            if isinstance(this_node.data, int):
                curr += d
            this_node = this_node.next
        return curr
    def average(self):
        sum = float(self.sum())
        count = float(self.length())
        return sum / count

numbers = LinkedList()
numbers.add(5)
numbers.add(8)
numbers.add(12)

names = LinkedList()
names.add("Ada")
names.add("Linus")
names.add("Guido")

empty = LinkedList()

print("numbers:", repr(numbers))
print("names  :", repr(names))
print("empty  :", repr(empty))

print()
print("length of numbers:", numbers.length())
print("length of names  :", names.length())
print("length of empty  :", empty.length())

print()
print("search(8)   ->", numbers.search(8))
print("search(8)   ->", numbers.search(8).get_data())
print("search(99)  ->", numbers.search(99))
print("search Ada  ->", names.search("Ada").get_prev().get_data())

print()
node = numbers.search(8)
print("node 8, prev:", node.get_prev().get_data())
print("node 8, next:", node.get_next().get_data())

print()
print("remove(8)  ->", numbers.remove(8))
print("numbers now:", repr(numbers), "| length:", numbers.length())

print("remove(12) ->", numbers.remove(12))
print("numbers now:", repr(numbers), "| length:", numbers.length())

print("remove(99) ->", numbers.remove(99))
print("numbers now:", repr(numbers), "| length:", numbers.length())

print()
numbers.add(42)
print("after add(42):", repr(numbers), "| length:", numbers.length())
print(numbers.search(5).get_next())
print(numbers.length())
print(numbers)
print((numbers.head))
print(numbers.sum())
print(numbers.average())