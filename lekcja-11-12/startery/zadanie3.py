# Temat 6. Zadanie 3. Kalkulator przesyłki, szkolne
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: czy_masa_poprawna(masa: float) -> bool zwraca True dla 0 < masa <= 20, w pozostałych przypadkach False.
# TODO: cena_przesylki(masa: float) -> float przyjmuje już sprawdzoną masę: do 1 kg włącznie koszt 12.00 zł, powyżej 1 do 5 kg włącznie 18.00 zł, powyżej 5 do 20 kg włącznie 30.00 zł. Są to umowne dane ćwiczenia.
# TODO: opis_przesylki(masa: float, cena: float) -> str zwraca napis Masa: {masa:.2f} kg, koszt: {cena:.2f} zł.
# TODO: Program główny wczytuje float(input(...)), ponawia odczyt, dopóki masa jest poza zakresem, następnie wywołuje funkcję ceny i funkcję opisu oraz wypisuje raport. Użytkownik wpisuje skończone liczby, z kropką jako separatorem dziesiętnym. Obsługa nienumerycznego tekstu jest poza zakresem tej lekcji.

def czy_masa_poprawna(masa: float) -> bool:
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def cena_przesylki(masa: float) -> float:
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def opis_przesylki(masa: float, cena: float) -> str:
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
