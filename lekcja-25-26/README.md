# Ćwiczenia: Praktyczny sprawdzian umiejętności: podstawy programowania, kolekcje danych, funkcje i standard PEP 8

**Temat 13 | Lekcje 25-26**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Koszt biletów

1. Napisz `oblicz_koszt(liczba, cena=12)`, zwracającą koszt zakupu biletów. Dla `liczba <= 0` funkcja zwraca 0. Dla pozostałych danych zwraca iloczyn liczby biletów i ceny. Przyjmij poprawną dodatnią cenę.
2. Program główny wczytuje całkowitą liczbę biletów. Jeśli jest niedodatnia, wyświetla zrozumiały komunikat i nie oblicza kosztów.
3. Dla poprawnej liczby wyświetla koszt standardowy z ceną domyślną 12 zł oraz ulgowy po przekazaniu ceny 8 zł. Wyniki mają opisy i jednostkę „zł”.
4. Funkcja przyjmuje dane w argumentach i zwraca wynik; nie używa `input()` ani `print()`.

| Wywołanie / wejście | Oczekiwany rezultat |
|---|---|
| `oblicz_koszt(3)` | 36 |
| `oblicz_koszt(3, 8)` | 24 |
| `oblicz_koszt(0)` | 0 |
| `oblicz_koszt(-2)` | 0 |
| W programie głównym: 1 | koszty 12 zł i 8 zł |
| W programie głównym: 0 lub -2 | komunikat o dodatniej liczbie biletów |

## Zadanie 2. Raport zakupów

Użyj listy krotek `(produkt, ilosc)`:

```python
zakupy = [
    ("zeszyt", 2),
    ("dlugopis", 1),
    ("zeszyt", 3),
    ("gumka", 1),
    ("dlugopis", 2)
]
```

1. Napisz `podsumuj(zakupy)`, zwracającą słownik z łączną liczbą sztuk każdego produktu. Nazwy powtarzają się, więc ich ilości trzeba dodawać. Dla pustej listy zwróć `{}`. Funkcja nie zmienia otrzymanej listy.
2. Wywołaj funkcję i pokaż raport przed zmianą danych. Następnie do listy dopisz krotkę `("gumka", 2)` i ponownie oblicz raport.
3. Po dopisaniu wyświetl każdy produkt i jego sumę w kolejności alfabetycznej nazw.
4. Użyj zbioru do obliczenia liczby różnych produktów i wyświetl ją. Wyświetl również łączną liczbę wszystkich sztuk.
5. Sprawdź `podsumuj([])`. Liczba pozycji na liście, liczba różnych produktów i liczba sztuk to różne wartości.

| Produkt | Sztuki przed dopisaniem | Sztuki po dopisaniu |
|---|---:|---:|
| dlugopis | 3 | 3 |
| gumka | 1 | 3 |
| zeszyt | 5 | 5 |

Po dopisaniu: 6 pozycji na liście, 3 różne produkty, 11 sztuk łącznie. Nie wymagamy wyświetlenia liczby pozycji, ale nie wolno użyć jej jako liczby sztuk.

## Zadanie 3. Analiza tekstu

1. Napisz `analizuj_tekst(tekst, minimalna_dlugosc=4)`, zwracającą słownik liczby wystąpień słów spełniających warunek długości.
2. Zamień tekst na małe litery i podziel według białych znaków. Ze skrajów każdego fragmentu usuń znaki `.,!?;:`. Nie usuwaj znaków ze środka słów.
3. Uwzględniaj słowa mające co najmniej `minimalna_dlugosc` znaków po oczyszczeniu. Minimalna długość jest dodatnią liczbą całkowitą.
4. Program wczytuje tekst i wyświetla wynik dla domyślnej długości, alfabetycznie według słów. Ponumeruj pozycje przez `enumerate`, zaczynając od 1. Dla pustego wyniku pokaż komunikat.
5. Sprawdź też funkcję z minimalną długością 3 i z pustym napisem. Funkcja nie wykonuje operacji wejścia-wyjścia.

Tekst kontrolny:

```text
Python, python! kod i TEST. test? Python.
```

| Parametry funkcji | Oczekiwany słownik |
|---|---|
| Tekst kontrolny, domyślna długość 4 | `{'python': 3, 'test': 2}` |
| Tekst kontrolny, długość 3 | `{'python': 3, 'kod': 1, 'test': 2}` |
| `""`, domyślna długość | `{}` |
| `"!!! i a"`, domyślna długość | `{}` |

Kolejność kluczy w zwracanym słowniku nie ma znaczenia dla oceny. Alfabetyczna kolejność dotyczy wyświetlenia: `1. python: 3`, `2. test: 2` dla domyślnego wywołania.

## Zadanie 4. NWD metodą Euklidesa

Adaptacja części konsolowej INF.04-01-23.01-SG. Wymagamy algorytmu z odejmowaniem, zgodnego z oryginalnym schematem. Nazwy `a` i `b` są wymagane w tym algorytmie i mają znaczenie matematyczne.

1. Utwórz funkcję `nwd(a, b)` z dwoma argumentami, zwracającą NWD dodatnich liczb całkowitych. W funkcji nie umieszczaj `input()` ani `print()`.
2. Implementacja: dopóki liczby są różne, porównuj je. Jeśli `a > b`, zastąp `a` przez `a - b`; w przeciwnym razie zastąp `b` przez `b - a`. Po zakończeniu zwróć `a`.
3. Program główny wczytuje dwie liczby i sprawdza, czy obie są dodatnie. Dla niepoprawnego zakresu wyświetla komunikat bez wywoływania funkcji. Dla poprawnych danych wyświetla opisany wynik.
4. Nad funkcją zapisz komentarz opisujący nazwę, parametry, działanie, wynik i autora i udokumentuj uruchomienie.

Nie zastępuj algorytmu przez modulo, `math.gcd` ani inną implementację NWD. Sama zgodność wyniku nie potwierdza zgodności z poleceniem.

| Dane programu głównego | Wynik / działanie |
|---|---|
| 48, 18 | 6 |
| 18, 48 | 6 |
| 7, 7 | 7 |
| 13, 5 | 1 |
| 1, 9 | 1 |
| 0, 5 lub -3, 6 | komunikat, brak wywołania `nwd` |

Warunkiem wywołania `nwd` są dwa dodatnie argumenty. Nie testuj samej funkcji dla zera: w tej wersji algorytmu mogłoby to prowadzić do nieskończonej pętli. Kontrola zakresu należy do programu głównego.

## Zadanie 5. Dla chętnych: Losowe wyniki (opcjonalne, diagnostyczne)

Napisz `losuj_wyniki(ile=6)`, zwracającą listę wyników losowania liczb całkowitych od 1 do 6 przez `random.randint`. Wywołaj ją domyślnie i dla 3 losowań. Wyświetl ponumerowane wyniki, sumę i liczbę różnych wyników. Powtórzenia są dozwolone. Zakładamy dodatnią liczbę losowań. Nie wymaga się konkretnej sekwencji; sprawdzamy długość i zakres wartości.

Zadanie nie zwiększa puli i nie jest wymagane do najwyższej oceny z części obowiązkowej.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
