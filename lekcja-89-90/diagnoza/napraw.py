def posortuj(dane):
    wynik = dane.copy()
    for i in range(len(wynik)):
        for j in range(len(wynik) - 1 - i):
            if wynik[j] < wynik[j + 1]:
                wynik[j], wynik[j + 1] = wynik[j + 1], wynik[j]
    return wynik
