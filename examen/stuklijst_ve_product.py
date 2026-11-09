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
    for onderdeel, aantal in samenstelling[artikel]
        curr += aantal +


if __name__ == "__main__":
    samenstelling = {
        'FIETS': [['WIEL', 2], ['FRAME', 1]],
        'WIEL': [['SPAAK', 32], ['NAAF', 1]],
    }
    prijzen = {'SPAAK': 0.50, 'NAAF': 12.00, 'FRAME': 67.00}

    print(totale_kost(samenstelling, prijzen, "FIETS"))
