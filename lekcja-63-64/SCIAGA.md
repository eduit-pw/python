# Temat 31. Wyjaśnienia do praktyki

## Podstawa systemu

Cyfra na pozycji oznacza wielokrotność potęgi podstawy. W systemie binarnym dopuszczone są tylko 0 i 1. Ten sam napis w innej podstawie może oznaczać inną wartość.

## Konwersje wbudowane

int(napis, podstawa) odczytuje wartość. bin, oct i hex zwracają napisy z prefiksami. format pozwala wyświetlić zapis bez prefiksu. Funkcja przeliczająca ma zwracać wynik o ustalonym typie.

## Schemat Hornera

Przetwarzaj cyfry od lewej: wynik = wynik * podstawa + cyfra. Zacznij od 0. Sprawdź pusty napis i niedozwolony znak przed uznaniem liczby za poprawną.

## Dzielenie z resztą

Kolejne reszty n % 2 są cyframi od najmniej znaczącej. Po n //= 2 przechodzisz do następnego kroku. Na końcu odwróć kolejność cyfr. Zero wymaga wyniku "0".

## Wielomian

Współczynniki podaj od najwyższej potęgi, także zera przy brakujących wyrazach. Aktualizacja wynik = wynik * x + wspolczynnik daje wartość wielomianu bez osobnego liczenia każdej potęgi.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
