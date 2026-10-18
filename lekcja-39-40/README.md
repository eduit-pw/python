# Ćwiczenia: Własne mechanizmy przeglądania elementów i generatory oszczędzające pamięć (yield)

**Temat 20 | Lekcje 39-40**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Przeglądanie ocen

**Cel:** `iter`, `next`, wyczerpanie i ponowne przeglądanie listy.

Dane: `oceny = [2, 4, 5]`.

1. Utwórz iterator listy.
2. Wypisz trzy kolejne oceny osobnymi wywołaniami `next`.
3. W czwartym wywołaniu użyj wyniku domyślnego `"KONIEC"`.
4. Wypisz samą listę, a następnie pierwszy element nowego iteratora tej listy.
5. W komentarzu odpowiedz: czy pobieranie elementów usunęło je z listy?

Oczekiwany wynik:

```text
2
4
5
KONIEC
[2, 4, 5]
2
```

**Dodatkowe próby:** `[]` oraz `[5]`. Pobieraj z wynikiem domyślnym i wskaż moment wyczerpania.

## Zadanie 2. Generator odliczania

**Cel:** `yield` i granica zakończenia.

1. Napisz generator `odliczaj(n)`, który oddaje kolejne liczby od `n` do 1 włącznie.
2. Dla `n <= 0` nie oddaje żadnej liczby. Zakładamy, że `n` jest liczbą całkowitą.
3. Wyświetl wyniki dla `n = 4` pętlą `for`, po jednej liczbie w wierszu.
4. Sprawdź wyniki przez `list(odliczaj(n))` dla poniższych przypadków.

| `n` | Oczekiwana lista |
|---|---|
| 4 | `[4, 3, 2, 1]` |
| 1 | `[1]` |
| 0 | `[]` |
| -2 | `[]` |

**Wskazówka 1:** warunek `while n > 0`. **Wskazówka 2:** zmiana `n` następuje po `yield`.

## Zadanie 3. Liczby parzyste w przedziale

**Cel:** generator z klasyczną pętlą i warunkiem.

Napisz `parzyste_od_do(start, stop)`. Argumenty są całkowite. Generator oddaje liczby parzyste od `start` do `stop` **włącznie**, w kolejności rosnącej. Jeśli `start > stop`, nie oddaje elementów. Nie buduj listy wynikowej wewnątrz generatora.

1. Użyj `for` i `range`, następnie `if` z resztą z dzielenia.
2. W programie głównym wyświetl elementy dla przedziału od -3 do 5, po jednym w wierszu.
3. Sprawdź pozostałe przypadki z tabeli.
4. Wyjaśnij w komentarzu, dlaczego prawą granicę zapisujesz jako `stop + 1`.

| Argumenty | Oczekiwany wynik przez `list(...)` |
|---|---|
| -3, 5 | `[-2, 0, 2, 4]` |
| 2, 2 | `[2]` |
| 3, 3 | `[]` |
| 5, 1 | `[]` |

**Wskazówka:** liczba jest parzysta, gdy `liczba % 2 == 0`.

## Zadanie 4. Analiza temperatur

**Cel:** połączenie generatora z licznikiem, sumatorem i minimum/maksimum.

Dane są już liczbami całkowitymi lub zmiennoprzecinkowymi:

```python
temperatury = [-60, -5, 0, 18, 70, 22]
```

1. Napisz generator `poprawne_temperatury(dane)`, który oddaje wyłącznie wartości z zakresu **od -50 do 60 włącznie**. Zachowaj kolejność. Nie modyfikuj danych wejściowych.
2. Napisz funkcję `analizuj_temperatury(dane)`. Przejdź po generatorze jeden raz. Użyj zwykłych zmiennych do wyznaczenia liczby przyjętych wartości, sumy, minimum i maksimum. W tym ćwiczeniu nie korzystaj z `sum`, `min`, `max` ani listy wszystkich poprawnych pomiarów.
3. Minimum i maksimum ustaw na pierwszy przyjęty pomiar. Po zakończeniu oblicz średnią, o ile przyjęto dane.
4. Gdy nie ma poprawnych pomiarów, wypisz `Brak poprawnych pomiarów.`. W innym przypadku wyświetl raport poniżej. Średnią sformatuj do dwóch miejsc po przecinku.

Oczekiwany raport dla podanych danych:

```text
Liczba pomiarów: 4
Suma: 35
Minimum: -5
Maksimum: 22
Średnia: 8.75
```

| Dane | Oczekiwany rezultat |
|---|---|
| `[]` | Brak poprawnych pomiarów. |
| `[-60, 70]` | Brak poprawnych pomiarów. |
| `[10]` | Liczba 1, suma 10, min/max 10, średnia 10.00 |
| `[-50, 60]` | Liczba 2, suma 10, min -50, max 60, średnia 5.00 |

**Wskazówka 1:** `for temperatura in poprawne_temperatury(dane):`.  
**Wskazówka 2:** po zwiększeniu licznika warunek `licznik == 1` rozpoznaje pierwszy przyjęty element.  
**Wskazówka 3:** sprawdź brak danych przed dzieleniem przez licznik.

## Zadanie 5. Dla chętnych: Iterator parzystych

Napisz klasę `ParzysteDo`, której obiekt jest iteratorem liczb `0, 2, 4, ...` aż do podanego całkowitego limitu włącznie.

- `__init__` zapisuje limit i bieżącą wartość 0.
- `__iter__` zwraca `self` i **nie resetuje** wartości bieżącej.
- `__next__` przy wyczerpaniu zgłasza `StopIteration`; w innym przypadku zapisuje wynik, zwiększa bieżącą wartość o 2 i oddaje wynik.
- Przetestuj `list(ParzysteDo(5)) == [0, 2, 4]`, limit 0, limit -1 i dwa przejścia po tej samej instancji. Po wyczerpaniu drugie przejście daje `[]`.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
