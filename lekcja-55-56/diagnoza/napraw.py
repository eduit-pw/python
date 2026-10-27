def suma_pliku(sciezka):
    with open(sciezka, encoding="utf-8") as plik:
        return sum(int(wiersz) for wiersz in plik)
