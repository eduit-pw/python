# Ćwiczenia: Wyświetlanie danych na stronach w Django: szablony HTML i przekazywanie informacji do widoku

**Temat 52 | Lekcje 107-108**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Kontynuacja projektu i dane widoku

Skopiuj działający `szkola_web` z poprzedniej lekcji do bieżącego folderu bez .venv. Uruchom go tym samym interpreterem. Utwórz katalog `strony/templates/strony/`. Lista początkowa to `["Programowanie w C#", "Angular dla początkujących", "Kurs Django"]`. Widok przekazuje ją w kontekście pod kluczem `kursy`. Szablony: `base.html`, `kursy.html`, `kontakt.html`; szablony podstron korzystają z extends i bloku treści. Zachowaj nazwy URL `kursy` i `kontakt`.

## Zadanie 1. Dynamiczna lista

- Utwórz widok kursy, trasę /kursy/ i szablon listy trzech nazw podanych powyżej.
- Wyświetl liczbę elementów oraz listę numerowaną. Dopisz czwarty kurs w widoku.
- Liczba oraz liczba pozycji mają zmienić się bez ręcznej zmiany HTML. Adaptacja motywu INF.04-02-22.06-SG, II: wyświetlanie w Django.

**Wynik kontrolny:** najpierw 3, następnie 4 kursy.

## Zadanie 2. Pusta lista

- Zastąp listę kursów przez []. Użyj {% empty %} do pokazania „Brak kursów”.
- Nagłówek nadal pokazuje liczbę. Nie dodawaj danych zastępczych w widoku.

**Wynik kontrolny:** liczba 0 i czytelny komunikat.

## Zadanie 3. Dwie strony, jeden układ

- Utwórz base.html z dokumentem HTML i linkiem do kursów przez {% url %}.
- Niech kursy.html i kontakt.html dziedziczą ten układ.
- Zmień podpis linku tylko w base.html i sprawdź obie strony.

**Wynik kontrolny:** zmiana widoczna w obu szablonach.

## Zadanie 4. Tekst zawierający znaczniki

- Przekaż tytul="<b>Oferta</b>" i wyświetl go przez {{ tytul }}.
- Sprawdź treść strony i jej źródło. Nie używaj safe ani autoescape off.

**Wynik kontrolny:** widoczny tekst `<b>Oferta</b>`, bez pogrubienia.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
