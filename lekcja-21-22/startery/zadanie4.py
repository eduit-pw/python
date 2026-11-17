# Temat 11. Zadanie 4. Dla chętnych: Suma kontrolna i cyfra płci PESEL - adaptacja INF.04-01-24.01-SG
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Zainicjuj tekst pesel = "55030101193" i sprawdź jego sumę, następnie wczytaj nowy tekst.
# TODO: Napisz poprawny_format(pesel): True wyłącznie dla 11 znaków od "0" do "9". Przy złym formacie program główny wypisuje komunikat i nie wywołuje dwóch pozostałych funkcji.
# TODO: Napisz okresl_plec(pesel): "K", gdy int(pesel[9]) jest parzyste; "M" w przeciwnym razie.
# TODO: Napisz sprawdz_sume(pesel). Dla pierwszych dziesięciu cyfr użyj wag [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]. Oblicz sumę iloczynów S, M = S % 10, R = 0 dla M == 0 lub R = 10 - M w innym przypadku. Zwróć wynik porównania R z int(pesel[10]).

def poprawny_format(pesel):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def sprawdz_sume(pesel):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def okresl_plec(pesel):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
