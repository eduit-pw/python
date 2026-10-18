# Ćwiczenia: Widoczność zmiennych w programie, wartości domyślne i funkcje z dowolną liczbą argumentów (*args, **kwargs)

**Temat 7 | Lekcje 13-14**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Przelicznik punktów, szkolne

**Polecenie:** napisz przelicz_punkty(punkty, mnoznik=1, *, premia=0). Parametry są liczbami całkowitymi. Dla punkty >= 0, mnoznik >= 1 i premia >= 0 zwróć punkty * mnoznik + premia. Dla niepoprawnego zakresu zwróć None. Funkcja nie odczytuje danych i nie wypisuje komunikatów. W programie głównym wykonaj testy z tabeli. Po wywołaniu dla zmiennej punkty = 10 sprawdź, że nadal ma ona wartość 10.

| Wywołanie | Wynik |
|---|---|
| przelicz_punkty(10) | 10 |
| przelicz_punkty(10, 2, premia=3) | 23 |
| przelicz_punkty(premia=3, punkty=10, mnoznik=2) | 23 |
| przelicz_punkty(-1) | None |
| przelicz_punkty(10, 0) | None |
| przelicz_punkty(10, premia=-1) | None |

## Zadanie 2. Raport pomiarów, szkolne

**Polecenie:** napisz raport_pomiarow(*odczyty, jednostka="V", precyzja=2). Odczyty są liczbami, jednostka napisem, precyzja liczbą całkowitą od 0 do 3. Przy braku odczytów zwróć dokładnie [BRAK POMIARÓW]. W innym przypadku oblicz sumę jawną pętlą for i zwróć trzy linie: liczba pomiarów, suma i średnia. Suma i średnia mają precyzja miejsc po kropce i jednostkę. Opcje podawaj po nazwie. Na tej lekcji zakładamy poprawne typy i zakres precyzji.

Dla raport_pomiarow(12.5, 11.8, 12.1, 12.2):

```text
Liczba: 4
Suma: 48.60 V
Średnia: 12.15 V
```

Dla raport_pomiarow(2, 4, jednostka="A", precyzja=1):

```text
Liczba: 2
Suma: 6.0 A
Średnia: 3.0 A
```

## Zadanie 3. Raport incydentu, szkolne

**Polecenie:** napisz raport_incydentu(kod, poziom="OSTRZEZENIE", **parametry). kod, poziom i wartości dodatkowych parametrów są napisami. Usuń otaczające białe znaki kodu; poziom oczyść i zamień na wielkie litery. Dopuszczalne poziomy to INFO, OSTRZEZENIE, KRYTYCZNY. Pusty kod lub inny poziom oznacza zwrot None. Dla poprawnych danych zwróć nagłówek [POZIOM] kod oraz osobną linię nazwa: wartość dla każdego dodatkowego parametru w kolejności podania. Dozwolone są dowolne dodatkowe nazwy. Funkcja nie wypisuje raportu; robi to program główny. Nie używaj global.

Pierwszy test:

```python
raport_incydentu(" ERR502 ", poziom="krytyczny",
                 host="PC1", port="443")
```

Oczekiwany raport:

```text
[KRYTYCZNY] ERR502
host: PC1
port: 443
```

Pozostałe testy:

| Wywołanie | Wynik |
|---|---|
| raport_incydentu("E1") | [OSTRZEZENIE] E1 |
| raport_incydentu("OK", poziom=" info ") | [INFO] OK |
| raport_incydentu("   ") | None |
| raport_incydentu("E1", poziom="AUDYT") | None |

## Zadanie 4. NWD i kontrakt funkcji, adaptacja INF.04

**Źródło algorytmu:** INF.04-01-23.01-SG, część I. Użyj odejmowania, nie modulo ani math.gcd.

**Polecenie:** utwórz nwd(a, b) dla dodatnich liczb całkowitych. Dopóki a i b są różne, odejmuj mniejszą od większej; zwróć a po zakończeniu. Funkcja ma dokładnie dwa argumenty i nie korzysta z input ani print. Program główny wczytuje obie liczby przez int(input(...)), a dla wartości <= 0 ponawia odczyt. Użytkownik wpisuje zapisy liczb całkowitych; obsługa tekstu nienumerycznego jest poza zakresem lekcji. Wypisz wynik z komunikatem. Dodaj komentarz nad funkcją według wzoru z arkusza: nazwa, opis, parametry, zwracany typ i opis, autor. Na lekcji jako autora wpisz identyfikator ucznia.

| a | b | NWD |
|---:|---:|---:|
| 48 | 18 | 6 |
| 18 | 48 | 6 |
| 7 | 7 | 7 |
| 13 | 8 | 1 |
| 1 | 9 | 1 |

Ślad dla (48, 18): (48, 18) → (30, 18) → (12, 18) → (12, 6) → (6, 6). Zwracana wartość: 6. Gdy argumenty od początku są równe, pętla nie wykona się ani razu. Zero lub liczba ujemna nie należą do kontraktu algorytmu; trzeba je odrzucić przed wywołaniem.

## Zadanie 5. Dla chętnych: Niezależne tagi - opcjonalne / domowe

**Polecenie:** popraw dodaj_blednie(tag, tagi=[]), używając None. Funkcja ma tworzyć nową listę po pominięciu tagi, ale dopisywać do listy przekazanej jawnie. Sprawdź trzy przypadki: dodaj_tag("siec"), dodaj_tag("system"), a następnie wspolne = ["start"] i dodaj_tag("test", wspolne). Po ostatnim wywołaniu wyświetl wspolne. Wyjaśnij, dlaczego wzorzec None nie oznacza kopiowania podanej listy.

Utwórz własną funkcję `dodaj_tag(tag, tagi=None)`: gdy lista nie została podana, utwórz nową. Dodaj tag i zwróć listę. Dwa niezależne wywołania mają dać `["siec"]` i `["system"]`. Dla przekazanej listy `["start"]` i tagu `"test"` wynik i przekazana lista mają zawierać `["start", "test"]`.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
