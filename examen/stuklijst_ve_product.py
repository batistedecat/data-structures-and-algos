def totale_kost(samenstelling, prijzen, artikel):
    if artikel not in samenstelling:
        return prijzen.get(artikel, 0)
    curr = 0
    for onderdeel, aantal in samenstelling[artikel]:
        curr += aantal * totale_kost(samenstelling, prijzen, onderdeel)
    return round(curr, 2)

def aantal_basisonderdelen(samenstelling, artikel):
    if artikel not in samenstelling:
        return 1
    curr = 0
    for onderdeel, aantal in samenstelling[artikel]:
        curr += aantal * aantal_basisonderdelen(samenstelling, onderdeel)
    return curr

def bevat(samenstelling, artikel, gezocht):
    if artikel == gezocht:
        return True
    if artikel not in samenstelling:
        return False
    for onderdeel, aantal in samenstelling[artikel]:
        if bevat(samenstelling, onderdeel, gezocht):
            return True
    return False

if __name__ == "__main__":
    samenstelling = {
        'FIETS': [['WIEL', 2], ['FRAME', 1]],
        'WIEL': [['SPAAK', 32], ['NAAF', 1]],
    }
    prijzen = {'SPAAK': 0.50, 'NAAF': 12.00, 'FRAME': 67.00}

    print(totale_kost(samenstelling, prijzen, "FIETS"))
    print(aantal_basisonderdelen(samenstelling, "FIETS"))
    print(bevat(samenstelling, "FIETS", "WIEL"))