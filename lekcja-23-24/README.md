# Ćwiczenia: Krótkie funkcje jednorazowe (lambda), przekształcanie list oraz losowanie liczb i moduł matematyczny

**Temat 12 | Lekcje 23-24**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Rabat i wybór cen

1. Użyj listy `ceny = [20, 50, 100]`.
2. Pętlą zbuduj nową listę cen po rabacie 10%. Nie zmieniaj listy wejściowej.
3. Drugą pętlą wybierz z wyniku ceny mniejsze niż 50 zł. Wyświetl obie listy i dane wejściowe.
4. Na podstawie przykładów `map` i `filter` wyjaśnij, jak otrzymać te same listy krótszym zapisem. Porównaj wyniki obu sposobów.

Kontrola: po rabacie `[18.0, 45.0, 90.0]`, wybrane `[18.0, 45.0]`. Puste wejście daje dwie puste listy. Wybór odbywa się po rabacie, a nie przed nim.

## Zadanie 2. Produkty według ceny

```python
produkty = [
    ("zeszyt", 7),
    ("dlugopis", 3),
    ("gumka", 3)
]
```

1. Utwórz nową listę przez `sorted`, przekazując lambdę zwracającą cenę, czyli drugi element krotki.
2. Wyświetl nazwy i ceny w kolejności rosnącej ceny. Zachowaj listę wejściową.
3. Sprawdź produkty o równej cenie. Ich wcześniejsza kolejność ma pozostać taka sama.
4. Zapisz też nazwany klucz ceny przez `def` i porównaj wyniki obu wersji.

Kontrola: `dlugopis 3`, `gumka 3`, `zeszyt 7`. Oryginalna lista nadal zaczyna się od zeszytu. Lambda jest tu wymagana jako cel ćwiczenia składni, nie jako ogólny warunek egzaminów INF.04.

## Zadanie 3. Pole i obwód koła

1. Napisz `parametry_kola(promien)`, zwracającą krotkę `(pole, obwod)`. Użyj `math.pi`, wzorów `pi * r ** 2` i `2 * pi * r`. Funkcja nie wykonuje `input()` ani `print()`.
2. Program główny wczytuje promień przez `float`. Przyjmujemy poprawny zapis skończonej liczby rzeczywistej.
3. Dla ujemnego promienia wyświetl komunikat bez wywoływania funkcji. W pozostałych przypadkach rozpakuj krotkę i wyświetl opisane wyniki z dwiema cyframi po kropce.
4. Sprawdź 0, 3 i -1. Funkcja otrzymuje tylko promień nieujemny.

| Promień | Oczekiwane wyświetlenie |
|---|---|
| 0 | Pole: 0.00, Obwód: 0.00 |
| 3 | Pole: 28.27, Obwód: 18.85 |
| -1 | komunikat o niedopuszczalnym promieniu |

## Zadanie 4. Loteria liczbowa INF.04

Adaptacja części konsolowej **INF.04-01-25.06-SG**. W Pythonie realizujemy ją strukturalnie. Zakres aplikacji zachowuje losowanie wielu zestawów i raport wystąpień. Kontrola dodatniości liczby zestawów, konkretne nazwy funkcji oraz ćwiczenie algorytmu z `while` są doprecyzowaniem szkolnym.

1. Wczytaj całkowitą liczbę zestawów. Dla niedodatniej liczby pokaż komunikat. Przyjmujemy poprawny zapis liczby całkowitej.
2. `generuj_zestawy(ile)` zwraca listę zestawów. Każdy zawiera sześć różnych liczb całkowitych od 1 do 49 włącznie. Listę nowego zestawu twórz wewnątrz pętli. W tym ćwiczeniu użyj `random.randint`, `while` i sprawdzania przynależności.
3. `wyswietl_zestawy(zestawy)` wyświetla wszystkie zestawy z numerami od 1. Kolejność liczb wewnątrz zestawu jest dowolna.
4. `zlicz_wystapienia(zestawy)` zwraca słownik liczników dla wszystkich liczb 1-49. Wyświetl także zera. Liczba może wystąpić w różnych zestawach, ale tylko raz w danym zestawie.
5. Dane przekazuj argumentami i zwracaj z funkcji. W funkcjach nie odczytuj zmiennych globalnych. Funkcja wyświetlająca zgodnie z nazwą używa `print`, pozostałe funkcje przetwarzające zwracają dane.
6. Dodaj nagłówek jednej funkcji oraz dokumentację opisaną w części „Oddanie pracy”.

**Testy własności:** dla `ile = 1` jest jeden zestaw, dla 3 są trzy. Każdy ma długość 6, sześć unikalnych wartości, wyłącznie całkowite wartości 1-49. Suma wszystkich liczników to `6 * ile`. Nie porównuj wyniku losowania z jedną z góry wybraną sekwencją.

**Test zliczania na stałych danych:**

```python
zestawy_kontrolne = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 7, 8, 49]
]
```

Liczby 1, 2 i 3 mają licznik 2. Liczby 4, 5, 6, 7, 8 i 49 mają licznik 1. Pozostałe mają 0. Suma to 12. Stałe dane służą tylko testowi funkcji zliczającej, a nie zastępują losowania w programie.

## Zadanie 5. Dla chętnych: Raport rzutów kostką (opcjonalne)

1. `losuj_rzuty(ile=20)` zwraca listę wyników z `random.randint(1, 6)`. Przyjmij dodatnie `ile`. Powtórzenia są dozwolone.
2. Napisz `zlicz_oczka(wyniki)`, zwracającą słownik liczników dla każdej wartości 1-6, także niewylosowanych.
3. Wyświetl wyniki, sześć liczników i średnią z dwiema cyframi po kropce. Suma liczników ma wynosić 20 dla domyślnego wywołania.
4. Sprawdź zliczanie dla `[1, 1, 6]`: 1 ma licznik 2, 6 ma 1, pozostałe 0, średnia 2.67.

To ćwiczenie autorskie. Nie utożsamiaj go z grą w kości z innych arkuszy: nie zawiera blokowania kości ani obliczania punktów gry.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
