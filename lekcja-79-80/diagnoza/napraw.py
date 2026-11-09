def horner(cyfry, podstawa):
    wynik = 0
    for cyfra in cyfry:
        wynik = wynik + podstawa * cyfra
    return wynik
