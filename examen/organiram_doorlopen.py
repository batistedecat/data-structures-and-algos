def aantal_medewerkers(knoop):
    if knoop["team"] == []:
        return 1
    curr = 1
    for member in knoop["team"]:
        curr += aantal_medewerkers(member)
    return curr

def diepte(knoop):
    if knoop["team"] == []:
        return 1
    curr = 1
    for member in knoop["team"]:
        curr = max(curr, diepte(member))
    return 1 + curr

def leidinggevende(knoop, naam):
    for member in knoop["team"]: #base case
        if member["naam"] == naam:
            return knoop["naam"]

    for member in knoop["team"]:
        boss = leidinggevende(member, naam)
        if boss is not None:
            return boss
    return None


if __name__ == "__main__":
    org = {'naam': 'Devos', 'team': [
        {'naam': 'Peeters', 'team': [
            {'naam': 'Maes', 'team': []},
            {'naam': 'Claes', 'team': []}]},
        {'naam': 'Janssens', 'team': [
            {'naam': 'Wouters', 'team': [
                {'naam': 'Aerts', 'team': []}]}]}]}

    print(aantal_medewerkers(org))
    print(diepte(org))
    print(leidinggevende(org, "Wouters"))