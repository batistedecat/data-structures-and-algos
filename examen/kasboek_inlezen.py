def schrijf_regels(path, lines):
    with open(path, "w", encoding="utf-8") as bestand:
        curr = 0
        for line in lines:
            bestand.write(line + "\n")
            curr += 1
        return curr


def lees_kasboek(path):
    rows = []
    skipped = 0
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                fields = line.split(";")
                if len(fields) != 3:
                    skipped += 1
                    continue
                datum, omschrijving, bedrag = [s.strip() for s in fields]
                try:
                    bedrag = float(bedrag)
                except ValueError:
                    skipped += 1
                    continue
                rows.append([datum, omschrijving, bedrag])
    except FileNotFoundError:
        return {"boekingen": [], "overgeslagen": 0}
    return {"boekingen": rows, "overgeslagen": skipped}


def saldo(path):
    try:
        f = open(path, encoding="utf-8")
        f.close()
    except FileNotFoundError:
        return None
    resultaat = lees_kasboek(path)
    totaal = 0.0
    for datum, omschrijving, bedrag in resultaat["boekingen"]:
        totaal += bedrag
    return round(totaal, 2)


if __name__ == "__main__":
    lines = ['# kasboek januari', '', '2026-01-03;huur;-950.00', '2026-01-05;verkoop;1240.50',
             'stuk;kapot', '2026-01-09;verkoop;veel', '2026-01-12;verkoop;310.25']

    print(schrijf_regels("kas.txt", lines))   # 7
    print(lees_kasboek("kas.txt"))            # 3 boekingen, overgeslagen: 2
    print(saldo("kas.txt"))                   # 600.75

    print(schrijf_regels("leeg.txt", []))     # 0
    print(lees_kasboek("leeg.txt"))           # {'boekingen': [], 'overgeslagen': 0}
    print(saldo("leeg.txt"))                  # 0.0

    print(lees_kasboek("bestaatniet.txt"))    # {'boekingen': [], 'overgeslagen': 0}
    print(saldo("bestaatniet.txt"))           # None