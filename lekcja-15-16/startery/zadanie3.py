# Temat 8. Zadanie 3. Dostawa i wycofywanie towarów
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Napisz znajdz_towar(baza, kod): pętla for po range(len(baza)), wynik pierwszy indeks albo -1.
# TODO: Napisz dostawa_towaru(baza, kod, dodana_ilosc). Dla dodatniej ilości i istniejącego kodu zwiększ baza[indeks][2] i zwróć True. W przeciwnym razie False, bez zmiany bazy.
# TODO: Napisz wycofaj_wyprzedane(baza). Usuń w miejscu wszystkie rekordy z ilosc <= 0 i zwróć liczbę usuniętych. Zastosuj while z kontrolowanym indeksem oraz pop(i). Zachowaj względną kolejność pozostałych.
# TODO: Funkcje nie wypisują. Dostawa i wycofanie celowo modyfikują argument. Po pop nie zwiększaj i, aby sprawdzić element, który zajął zwolnioną pozycję.

def znajdz_towar(baza, kod):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def dostawa_towaru(baza, kod, dodana_ilosc):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def wycofaj_wyprzedane(baza):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
