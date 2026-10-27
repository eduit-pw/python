# Temat 2. Wyjaśnienia do praktyki

## Nazwa, wartość i przypisanie

Zapis cena = 12 wiąże nazwę z obiektem liczbowym. Późniejsze przypisanie zastępuje to powiązanie. = służy do przypisania, a == do porównania.

## Cztery proste typy

int reprezentuje liczbę całkowitą, float przybliżoną liczbę rzeczywistą, str napis, a bool True albo False. type(wartosc) pozwala sprawdzić typ w czasie wykonania.

## input i konwersja

input(komunikat) wyświetla pytanie i zwraca str, nawet jeśli wpisano cyfry. int("12") daje 12, float("2.5") daje 2.5. Błędny zapis liczby powoduje ValueError.

## Identyfikatory jako tekst

Kod 00123, numer telefonu i PIN przechowuj jako str, gdy początkowe zera mają znaczenie. Konwersja całego kodu do int usuwa informację o liczbie początkowych zer.

## F-string i format wyniku

W f"Cena: {cena:.2f}" wyrażenie w nawiasach jest obliczane, a .2f daje dwie cyfry po kropce. Format 03d uzupełnia liczbę całkowitą zerami do szerokości co najmniej 3.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
