# De code van je collega. Ze is correct, maar onbruikbaar traag zodra het doel groter wordt.
# Herschrijf ze zodat ze hetzelfde antwoord geeft en wel schaalt.
from functools import cache

@cache
def aantal_scenarios(doel):
    if doel < 0:
        return 0
    if doel == 0:
        return 1
    return aantal_scenarios(doel - 1) + aantal_scenarios(doel - 2) + aantal_scenarios(doel - 5)

@cache
def min_stappen(doel):
    if doel < 0:
        return None
    if doel == 0:
        return 0
    mogelijk = []
    for stap in [1, 2, 5]:
        onder = min_stappen(doel - stap)
        if onder is not None:
            mogelijk.append(onder + 1)
    return min(mogelijk)

@cache
def traagste_stap():
    # Geef hier de letter terug van de belangrijkste oorzaak, zie de opgave.
    return '?'


if __name__ == "__main__": #test code made with Claude Opus
    import time

    # Original (slow) code as a reference, only for small values
    def scen_ref(d):
        if d < 0: return 0
        if d == 0: return 1
        return scen_ref(d - 1) + scen_ref(d - 2) + scen_ref(d - 5)

    def stap_ref(d):
        if d < 0: return None
        if d == 0: return 0
        mogelijk = []
        for s in [1, 2, 5]:
            onder = stap_ref(d - s)
            if onder is not None:
                mogelijk.append(onder + 1)
        return min(mogelijk)

    def leeg_cache():
        aantal_scenarios.cache_clear()
        min_stappen.cache_clear()

    def check(naam, kreeg, verwacht):
        status = "OK  " if kreeg == verwacht else "FOUT"
        print(f"{status} {naam}: kreeg {kreeg!r}, verwacht {verwacht!r}")

    print("--- Randgevallen ---")
    check("aantal_scenarios(-1)", aantal_scenarios(-1), 0)
    check("aantal_scenarios(-10)", aantal_scenarios(-10), 0)
    check("aantal_scenarios(0)", aantal_scenarios(0), 1)
    check("aantal_scenarios(1)", aantal_scenarios(1), 1)
    check("min_stappen(-1)", min_stappen(-1), None)
    check("min_stappen(0)", min_stappen(0), 0)
    check("min_stappen(1)", min_stappen(1), 1)

    print("\n--- Gewone gevallen ---")
    check("aantal_scenarios(5)", aantal_scenarios(5), 9)
    check("aantal_scenarios(10)", aantal_scenarios(10), 128)
    check("min_stappen(5)", min_stappen(5), 1)
    check("min_stappen(10)", min_stappen(10), 2)
    check("min_stappen(13)", min_stappen(13), 4)

    print("\n--- Vergelijking met de originele code (0 t.e.m. 20) ---")
    leeg_cache()
    fouten = 0
    for d in range(21):
        if aantal_scenarios(d) != scen_ref(d) or min_stappen(d) != stap_ref(d):
            print(f"FOUT bij doel={d}")
            fouten += 1
    print("OK   alle waarden gelijk" if fouten == 0 else f"FOUT {fouten} verschillen")

    print("\n--- Zeer grote gevallen (telkens met lege cache, zoals in Dodona) ---")
    for d in [500, 900, 1000, 5000, 100_000]:
        for f in (aantal_scenarios, min_stappen):
            leeg_cache()
            start = time.perf_counter()
            try:
                f(d)
                duur = time.perf_counter() - start
                print(f"OK   {f.__name__}({d}) in {duur:.4f} s")
            except RecursionError:
                print(f"FOUT {f.__name__}({d}): RecursionError (te diep)")

    print("\n--- Controle min_stappen voor groot doel ---")
    leeg_cache()
    check("min_stappen(950)", min_stappen(950), 190)