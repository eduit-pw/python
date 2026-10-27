# Temat 29. Wyjaśnienia do praktyki

## CSV i separator

CSV przechowuje pola tekstowe w rekordach. Separator może wystąpić wewnątrz pola ujętego w cudzysłowy. Dlatego użyj csv zamiast split(";").

## DictReader i konwersja

DictReader używa nagłówka jako nazw pól i zwraca wartości napisowe. int przekształca ilość dopiero po odczycie. Otwórz plik z newline="" i odpowiednim encoding.

## DictWriter

Podaj fieldnames, zapisz writeheader, a potem writerow lub writerows. Kolejność kolumn wynika z fieldnames. Użyj tego samego separatora, którego wymaga zadanie.

## JSON w pliku

json.load czyta strukturę z pliku, loads z napisu. dump zapisuje do pliku, dumps zwraca napis. ensure_ascii=False zachowuje czytelne polskie litery, indent dodaje wcięcia.

## Składnia i schemat

Poprawny JSON nie oznacza danych zgodnych z umową. Oddziel błąd składni JSON od brakującego pola, złego typu i zakresu. true w JSON jest bool, a nie poprawnym int w kontrakcie ścisłym.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
