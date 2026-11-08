def omzet_per_klant(verkopen):
    totaal = {}
    for klant, bedrag in verkopen:
        totaal[klant] = totaal.get(klant, 0) + bedrag
    return {klant: round(bedrag, 2) for klant, bedrag in totaal.items()}


def top_klanten(verkopen, k):
    if k <= 0:
        return []
    omzet = omzet_per_klant(verkopen)
    gesorteerd = sorted(omzet.items(), key=lambda x: (-x[1], x[0]))
    return [[klant, bedrag] for klant, bedrag in gesorteerd[:k]]

def klanten_boven(verkopen, drempel):
    omzet = omzet_per_klant(verkopen)
    temp = [key for key, val in omzet.items() if val > drempel]
    return sorted(temp)

if __name__ == "__main__":
    verkopen = [['Devos', 1200.50], ['Peeters', 800.00], ['Devos', 299.50],
                ['Maes', 950.00], ['Peeters', 400.00]]

    print(top_klanten(verkopen, 3))
    print(klanten_boven(verkopen, 1000))