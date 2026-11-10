

# voorbeeldexamen Algoritmen en datastructuren op dodona
# 10 november 2026
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


def read_purchases(path):
    rows = {}
    with open(path) as f:
        header = [h.strip() for h in f.readline().strip().split(";")]
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            fields = line.split(";")
            if len(fields) != len(header):
                continue
            article, date, quantity, unit_cost = [x.strip() for x in fields]
            quantity = int(quantity)
            unit_cost = float(unit_cost)
            if article not in rows:
                inv = Inventory(article)
                inv.add_batch(date, quantity, unit_cost)
                rows[article] = inv
            else:
                rows[article].add_batch(date, quantity, unit_cost)
        return rows
if __name__ == "__main__":
    regels = [
        "artikel;datum;aantal;eenheidsprijs",
        "A100;2026-01-03;50;2.40",
        "B200;2026-01-04;10;15.00",
        "",
        "# commentaar",
        "A100;2026-01-10;30;2.55",
        "C300;2026-01-11;-5;3.00",
        "kapot;regel",
        "B200;2026-01-12;20;14.50",
    ]
    with open("aankopen.csv", "w", encoding="utf-8") as f:
        for r in regels:
            f.write(r + "\n")

    voorraad = read_purchases("aankopen.csv")

    print(sorted(voorraad.keys()))
    for code, inv in voorraad.items():
        print(f"--- {code} ({inv.length} loten) ---")
        curr = inv.head
        while curr is not None:
            print(curr)
            curr = curr.next
        print("totaal aantal:", inv.total_quantity())
        print("totale waarde:", inv.total_value())