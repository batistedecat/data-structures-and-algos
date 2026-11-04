# voorbeeldexamen Algoritmen en datastructuren op dodona
# 4 november 2026
# Batiste Decat

#=============1==============
class Batch(): # heeft data en een pointer naar volgend object
    def __init__(self, date, quantity, unit_cost):
        self.next = None
        self.date = date
        self.quantity = quantity
        self.unit_cost = unit_cost

    def __str__(self):
        return f"{self.date}: {self.quantity} stuks aan {self.unit_cost} euro"

#=============2==============
class Inventory():
    def __init__(self, article):
        self.head = None
        self.tail = None
        self.article = article
        self.length = 0

    def add_batch(self, date, quantity, unit_cost):
        if quantity > 0 and unit_cost > 0:
            node = Batch(date, quantity, unit_cost)
            if self.head is None:
                self.head = node
            else:
                self.tail.next = node
            self.tail = node
            self.length += 1
            return True
        else:
            return False

    def total_quantity(self):
        curr = self.head
        quant = 0
        while curr is not None:
            quant += curr.quantity
            curr = curr.next
        return quant

    def total_value(self):
        curr = self.head
        val = 0
        while curr is not None:
            val += curr.quantity * curr.unit_cost
            curr = curr.next
        return val

    def find_batch(self, date):
        curr = self.head
        while curr != None:
            if curr.date == date:
                return curr
            curr = curr.next
        return None

#=============3==============
def main():
    inventory = Inventory(article = "BOLT-M6")
    inventory.add_batch(date = "2026-01-15", quantity = 100, unit_cost = 8.5)
    inventory.add_batch(date="2026-02-03", quantity=60, unit_cost=9)
    inventory.add_batch(date="2026-03-11", quantity=40, unit_cost=9.75)

    print(inventory.add_batch(date="2026-04-02", quantity=0, unit_cost=10))
    print(inventory.total_quantity())
    print(inventory.total_value())
    print(inventory.find_batch("2026-02-03"))
    print(inventory.find_batch("2026-12-31"))

if __name__ == "__main__":
    main()