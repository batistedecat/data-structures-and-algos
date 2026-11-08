# dodona oefening bij LinkedLists
# vak: algoritmen en datastructuren
# door: Batiste Decat
# datum: zondag 8 november 2026


# prio 1 > 2 > 3
class Ticket:
    # class Node:
    def __init__(self, klant, prioriteit):
        self.klant = klant
        self.prioriteit = prioriteit
        self.next = None


class Wachtrij:
    def __init__(self):
        self.first = None
        # self.tail = None
        self.length = 0

    def voeg_toe(self, klant, prioriteit):
        if (not klant) or prioriteit not in (1, 2, 3):
            return False
        node = Ticket(klant, prioriteit)
        if self.first is None or prioriteit < self.first.prioriteit:
            node.next = self.first
            self.first = node
            self.length += 1
            return True

        curr = self.first

        while curr.next is not None:
            if curr.next.prioriteit > prioriteit:
                node.next = curr.next
                curr.next = node
                self.length += 1
                return True
            curr = curr.next
        node.next = curr.next
        curr.next = node
        self.length += 1
        return True

    def haal_af(self):
        if self.length == 0:
            return None
        node = self.first
        self.first = node.next
        self.length -= 1
        return node.klant

    def aantal(self):
        return self.length

    def namen(self):
        ans = []
        curr = self.first

        while curr is not None:
            ans.append(curr.klant)
            curr = curr.next
        return ans

    def zoek(self, klant):
        curr = self.first
        while curr is not None:
            if klant == curr.klant:
                return curr
            curr = curr.next
        return None


if __name__ == "__main__":  # checks made by claude Opus
    fouten = 0


    def check(label, kreeg, verwacht):
        global fouten
        if kreeg == verwacht:
            print("OK   ", label)
        else:
            fouten += 1
            print("FOUT ", label, "| kreeg:", kreeg, "| verwacht:", verwacht)


    # empty queue
    w = Wachtrij()
    check("empty: aantal", w.aantal(), 0)
    check("empty: namen", w.namen(), [])
    check("empty: haal_af", w.haal_af(), None)

    # adding: empty queue, new front, same priority, at the end
    check("Maes 2 in empty queue", w.voeg_toe("Maes", 2), True)
    check("Peeters 1 becomes the front", w.voeg_toe("Peeters", 1), True)
    check("Claes 2 behind Maes", w.voeg_toe("Claes", 2), True)
    check("Wouters 3 at the end", w.voeg_toe("Wouters", 3), True)
    check("Janssens 1 behind Peeters", w.voeg_toe("Janssens", 1), True)
    check("order", w.namen(), ["Peeters", "Janssens", "Maes", "Claes", "Wouters"])
    check("aantal after 5 adds", w.aantal(), 5)

    # edge cases: False and nothing changes
    check("empty name", w.voeg_toe("", 1), False)
    check("None as name", w.voeg_toe(None, 1), False)
    check("priority 0", w.voeg_toe("Devos", 0), False)
    check("priority 4", w.voeg_toe("Devos", 4), False)
    check("queue unchanged", w.namen(), ["Peeters", "Janssens", "Maes", "Claes", "Wouters"])
    check("aantal unchanged", w.aantal(), 5)

    # removing: always the front
    check("haal_af 1", w.haal_af(), "Peeters")
    check("haal_af 2", w.haal_af(), "Janssens")
    check("aantal after 2 removes", w.aantal(), 3)
    check("Devos 1 becomes the front again", w.voeg_toe("Devos", 1), True)
    check("order after removing", w.namen(), ["Devos", "Maes", "Claes", "Wouters"])

    # empty it completely, then reuse
    for naam in ["Devos", "Maes", "Claes", "Wouters"]:
        check("haal_af " + naam, w.haal_af(), naam)
    check("empty again: haal_af", w.haal_af(), None)
    check("empty again: aantal", w.aantal(), 0)
    check("empty again: namen", w.namen(), [])
    check("Aerts 3 after emptying", w.voeg_toe("Aerts", 3), True)
    check("Goossens 3 behind Aerts", w.voeg_toe("Goossens", 3), True)
    check("order after reuse", w.namen(), ["Aerts", "Goossens"])

    print()
    print("All tests passed" if fouten == 0 else f"{fouten} test(s) failed")