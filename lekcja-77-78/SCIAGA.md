# Temat 38. Wyjaśnienia do praktyki

## date i datetime

date opisuje dzień kalendarzowy, datetime także czas. Nie dodawaj dni przez ręczną zmianę numeru miesiąca. Użyj timedelta.

## Parsowanie i formatowanie

strptime(napis, format) odczytuje datę z tekstu. strftime(format) tworzy tekst daty. %d oznacza dzień, %m miesiąc, %Y czterocyfrowy rok. Błędna data zgłasza ValueError.

## Różnica czasu

Odjęcie dwóch zgodnych datetime daje timedelta. total_seconds() obejmuje cały czas, a seconds jest tylko częścią składową. Minuty uzyskasz przez podzielenie całej liczby sekund przez 60.

## Przedziały dat

Przedział poczatek <= data < koniec ułatwia filtrowanie pełnego miesiąca. Początek włączasz, początek następnego miesiąca wykluczasz. Sprawdź obie granice.

## Strefy i umowa danych

Datetime bez tzinfo nie przechowuje strefy. W tych ćwiczeniach wspólny lokalny czas jest świadomym uproszczeniem. Dla danych z wielu stref trzeba ustalić sposób normalizacji.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
