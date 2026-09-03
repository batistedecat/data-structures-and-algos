class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self): #the node sequence after current node
        return f"{self.data} -> {str(self.next)}"

    def __repr__(self): #info in single node
        return f"[data: {self.data} | pointer: {str(self.next.data)}]"

class SingleLL:
    def __init__(self):
        self.head = None
        self.size = 0
    def __str__(self):
        if self.head == None:
            return "empty list"
        return str(self.head)

    def add(self, d): #adds on the head
        new_node = Node(d)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    def search(self, d):
        this_node = self.head
        while this_node:
            if this_node.data == d:
                return this_node
            this_node = this_node.next
        return None

numbers = SingleLL()
numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(4)
numbers.add(5)

print(numbers)
numbers.reverse()
print(numbers)
print(numbers.search(2))