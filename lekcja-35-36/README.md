# Ćwiczenia: Dziedziczenie: tworzenie klas pochodnych i ponowne wykorzystanie kodu klasy bazowej (super)

**Temat 18 | Lekcje 35-36**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Baza do wykorzystania

W pliku `urzadzenie.py` jest gotowa klasa `Urzadzenie(nazwa)` z polem `wlaczone = False`. `wlacz()` ustawia True, `wylacz()` ustawia False, a `opis()` zwraca `nazwa: włączone` albo `nazwa: wyłączone`. Importuj ją w plikach kolejnych zadań. Zadania 2-4 rozwijają wersję z poprzedniego zadania. Zapisz je w osobnych plikach `zadanie1.py` itd., aby móc odtworzyć każdy etap.

## Sposób pracy podczas bloku

| Etap | Czas | Co robisz |
| --- | ---: | --- |
| Wyjaśnienia i demonstracja | 0-25 min | Czytasz przykład, przewidujesz wynik i zadajesz pytania. |
| Zadanie 1 z prowadzącym | 25-35 min | Uruchamiasz pierwszy wariant i objaśniasz kluczowy zapis. |
| Zadanie 2 wspólnie | 35-50 min | Proponujesz kolejne kroki, sam zapisujesz kod. |
| Zadanie 3 samodzielnie | 50-70 min | Realizujesz kontrakt i wykonujesz próby. |
| Zadanie 4 lub diagnoza błędu | 70-85 min | Sprawdzasz przypadki graniczne i poprawiasz program. |
| Zakończenie | 85-90 min | Zapisujesz kod, jeden wniosek i wykonane próby. |

Tempo ustala nauczyciel. Jeśli zadanie 4 jest większe, stanowi kontynuację na kolejnych zajęciach lub zastępuje dodatkową diagnozę. Zadania dodatkowe nie są warunkiem ukończenia podstawowego bloku.

**Przed praktyką:** przeczytaj [ściągę](SCIAGA.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Odziedziczone metody i dwa obiekty

Użyj bazy `Urzadzenie` i `class Pralka(Urzadzenie): pass`.

1. Utwórz `p1 = Pralka("Pralka A")` i `p2 = Pralka("Pralka B")`.
2. Przed uruchomieniem zapisz wyniki `p1.opis()` oraz `p2.opis()`.
3. Włącz tylko `p1`, wyświetl opisy obu obiektów, a następnie wyłącz `p1` i ponownie wyświetl jego opis.
4. Wyjaśnij, skąd `Pralka` bierze metody i dlaczego zmiana `p1` nie włącza `p2`.

**Wyniki po włączeniu `p1`:** `Pralka A: włączone`, `Pralka B: wyłączone`. Po wyłączeniu: `Pralka A: wyłączone`. Początkowo obie pralki są wyłączone.  
**Wskazówka:** każde uruchomienie `__init__` przypisuje dane do konkretnego `self`.

## Zadanie 2. Program pralki

1. Dodaj do `Pralka` własne `__init__(self, nazwa)`. Użyj inicjalizacji bazy i ustaw `program = 1`.
2. Napisz `ustaw_program(self, numer)`. Dla całkowitego numeru z zakresu 1-5 ustawia program i zwraca `True`. Poza zakresem zwraca `False` i zachowuje dotychczasowy program. Przyjmujemy liczby całkowite; nie testujemy napisów, `None` ani `bool`.
3. Sprawdź stan początkowy i wywołania kolejno z wartościami `5`, `0`, `6`, `1`.
4. Sprawdź, że odziedziczone `wlacz()` nadal działa.

| Operacja | Wynik metody | Program po operacji |
|---|---|---|
| Utworzenie | nie dotyczy | `1` |
| `ustaw_program(5)` | `True` | `5` |
| `ustaw_program(0)` | `False` | `5` |
| `ustaw_program(6)` | `False` | `5` |
| `ustaw_program(1)` | `True` | `1` |

**Wskazówka:** w poprawnej gałęzi przypisz `self.program = numer` i zwróć wynik, a po niej zwróć `False`.

## Zadanie 3. Rozszerzony opis pralki

1. W klasie `Pralka` z zadania 2 nadpisz `opis(self)`.
2. Wywołaj opis z bazy przez `super().opis()` i dopisz `", program "` oraz numer programu.
3. Metoda ma zwracać napis. Nie powielaj warunku włączenia z klasy bazowej.
4. Sprawdź opis początkowy, następnie ustaw program 5, włącz pralkę i ponownie wyświetl opis. Zmień nazwę obiektu na `"Łazienka"` i sprawdź trzeci wynik.

**Wyniki dla początkowej nazwy `"Pralka"`:**

```text
Pralka: wyłączone, program 1
Pralka: włączone, program 5
Łazienka: włączone, program 5
```

**Wskazówka:** do połączenia napisu z liczbą użyj `str(self.program)` albo znanego f-stringa.

## Zadanie 4. Drugie urządzenie i raport

1. Zdefiniuj `Odkurzacz(Urzadzenie)`. Inicjalizuj stan bazy i własny atrybut `moc = 1`.
2. Napisz `ustaw_moc(self, poziom)`. Dopuszcza całkowite wartości 1-3. Poprawna wartość daje `True` i aktualizuje moc; błędna daje `False` bez zmiany mocy.
3. Nadpisz `opis()`, wykorzystując `super().opis()`. Dopisz `", moc "` oraz bieżącą moc.
4. Utwórz pralkę z zadania 3 i odkurzacz. Ustaw pralce program 5 i odkurzaczowi moc 3. Włącz tylko odkurzacz.
5. Wyświetl opisy obu obiektów w zwykłej pętli po liście. Wyłącz odkurzacz i wyświetl jego opis ponownie.
6. Sprawdź poziomy `0`, `4`, `1` i pustą listę raportu. Rozgałęzianie według typu obiektu nie jest potrzebne, ponieważ oba mają `opis()`.

**Wyniki raportu:**

```text
Pralka: wyłączone, program 5
Odkurzacz: włączone, moc 3
```

Po wyłączeniu: `Odkurzacz: wyłączone, moc 3`. Dla prób mocy `0`, `4`, `1` wyniki to `False`, `False`, `True`, a moc po każdej próbie to `3`, `3`, `1`. Pusta lista raportu nie daje wyjścia.  
**Wskazówka:** wykorzystaj układ klasy `Pralka`, ale zmień nazwę atrybutu i zakres. Nie kopiuj całej klasy bazowej do `Odkurzacz`.

## Zadanie 5. Dla chętnych: Urządzenie, które liczy włączenia

Utwórz `LiczaceUrzadzenie(Urzadzenie)` z licznikiem `liczba_wlaczen = 0`. Nadpisz `wlacz()`: zwiększ licznik tylko przy przejściu ze stanu wyłączonego do włączonego i użyj `super().wlacz()` do zmiany stanu. Kolejne `wlacz()` już włączonego obiektu nie zwiększa licznika.

**Testy:** stan początkowy: `False`, `0`; po pierwszym włączeniu: `True`, `1`; po drugim: `True`, `1`; po wyłączeniu i ponownym włączeniu: `True`, `2`.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
