# Temat 32. Wyjaśnienia do praktyki

## Alfabet i indeks

ord zwraca kod znaku, chr znak dla kodu. Po odjęciu ord("a") mała litera ma indeks 0-25. Po przesunięciu dodaj początek alfabetu i użyj chr.

## Modulo i klucz

(indeks + klucz) % 26 zawija wynik do alfabetu. Działa również dla klucza ujemnego i większego od 26. Spacje przepisz zgodnie z umową, zamiast przesuwać ich kod.

## Szyfr podstawieniowy

GADERYPOLUKI składa się z par GA, DE, RY, PO, LU, KI. Każdą parę zamieniasz w obie strony. Wielkość liter i pozostałe znaki obsługuj dokładnie według specyfikacji.

## Odwracalność

Cezara odszyfrujesz przeciwnym kluczem. Szyfr par zastosowany dwa razy daje wejście. Taki test własności uzupełnia stałe oczekiwane wyniki, ale ich nie zastępuje.

## Struktura programu

Funkcja szyfrująca przyjmuje tekst i klucz, zwraca str. Input i print są w programie głównym. Zapisuj literalne oczekiwania testów, żeby błędny algorytm nie produkował własnych odpowiedzi.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
