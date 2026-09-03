class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleLL:
    def __init__(self):
        self.head = None
        self.size = 0
    def __str__(self):
        curr = []
        this_node = self.head
        while this_node:
            curr.append(str(this_node.data))
            this_node = this_node.next
        return ', '.join(curr)

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

numbers = SingleLL()
numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(4)
numbers.add(5)

print(numbers)
numbers.reverse()
print(numbers)
