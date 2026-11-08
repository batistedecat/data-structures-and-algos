# De code van je collega. Ze is correct, maar te traag zodra er veel loten bijkomen.
# Herschrijf ze zodat ze hetzelfde doet en wel schaalt.

class Lot:
    def __init__(self, code, aantal):
        self.code = code
        self.aantal = aantal
        self.next = None


class Voorraad:
    def __init__(self):
        self.first = None
        self.tail = None #nieuw
        self.length = 0

    def voeg_achteraan(self, code, aantal):
        if aantal <= 0: #O(1)
            return False
        nieuw = Lot(code, aantal) # O(1)
        if self.first is None:
            self.first = nieuw
            self.tail = nieuw  #nieuw
            self.length += 1 # nieuw
            return True
        self.tail.next = nieuw # nieuw
        self.tail = nieuw # nieuw
        self.length += 1 # nieuw
        return True

    def aantal_loten(self):
        return self.length #nieuw

    def totaal_aantal(self):
        totaal = 0
        huidige = self.first
        while huidige is not None:
            totaal += huidige.aantal
            huidige = huidige.next
        return totaal


def traagste_stap():
    # Geef hier de letter terug van de belangrijkste oorzaak, zie de opgave.
    return 'B' # nieuw


if __name__ == "__main__": # test-code made by claude opus
    # Je eigen testen. Dodona voert dit blok niet uit.
    import time
    import matplotlib.pyplot as plt

    N = 50_000
    STAP = 100

    v = Voorraad()
    aantallen = []       # aantal loten na elke stap van 1000
    batch_tijden = []    # seconden voor die 1000 toevoegingen
    totaal_tijden = []   # seconden sinds de start

    start = time.perf_counter()
    batch_start = start
    for i in range(1, N + 1):
        v.voeg_achteraan(i, 1)
        if i % STAP == 0:
            nu = time.perf_counter()
            aantallen.append(i)
            batch_tijden.append(nu - batch_start)
            totaal_tijden.append(nu - start)
            batch_start = nu

    print(f"{N} loten toegevoegd in {totaal_tijden[-1]:.3f} s")
    print("aantal_loten:", v.aantal_loten(), "| totaal_aantal:", v.totaal_aantal())

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    ax1.plot(aantallen, batch_tijden, linewidth=1)
    ax1.set_title(f"Tijd per {STAP} toevoegingen")
    ax1.set_xlabel("aantal loten in de voorraad")
    ax1.set_ylabel("seconden")
    ax1.set_ylim(bottom=0)
    ax2.plot(aantallen, totaal_tijden, linewidth=1.5)
    ax2.set_title("Totale tijd sinds de start")
    ax2.set_xlabel("aantal loten in de voorraad")
    ax2.set_ylabel("seconden")
    ax2.set_ylim(bottom=0)
    plt.tight_layout()
    plt.show()