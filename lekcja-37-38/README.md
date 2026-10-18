# Ćwiczenia: Wspólny interfejs dla różnych obiektów oraz tworzenie klas wzorcowych (@abstractmethod)

**Temat 19 | Lekcje 37-38**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Klasy początkowe

Do zadania 1 zdefiniuj `Zwierze.glos()` zwracające `"?"`, `Pies(Zwierze).glos()` zwracające `"hau"` oraz `Kot(Zwierze).glos()` zwracające `"miau"`. W zadaniach 2-3 bazą jest:

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass
```

Zakładamy wymiary liczbowe. Wersja podstawowa dopuszcza zero. Każde zadanie zapisz w osobnym pliku i dodaj pokaz działania.

## Zadanie 1. Kolejne głosy

1. Przed uruchomieniem pętli dla `[Pies(), Kot(), Zwierze()]` zapisz przewidywane wyniki i klasy, których metody zostaną wykonane.
2. Dodaj klasę `Krowa(Zwierze)` z metodą `glos()` zwracającą `"muu"`.
3. Uruchom tę samą pętlę dla `[Kot(), Krowa(), Pies()]`, a następnie dla pustej listy.
4. Wyjaśnij, dlaczego dodanie krowy nie wymaga zmiany wnętrza pętli.

**Wyniki:** dla drugiej listy kolejno `miau`, `muu`, `hau`; dla pustej listy brak wyjścia.  
**Wskazówka:** skopiuj sposób nadpisania metody z klasy `Kot`, a następnie zmień wynik.

## Zadanie 2. Prostokąt bez pola

Użyj abstrakcyjnej `Figura` opisanej w przygotowaniu oraz poniższej niepełnej klasy:

```python
class Prostokat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b
```

1. Spróbuj utworzyć `Prostokat(3, 4)`. Zapisz typ i przyczynę błędu.
2. Uzupełnij `pole(self)`, aby zwracało iloczyn boków.
3. Wyświetl wyniki dla `(3, 4)`, `(0, 5)` oraz `(2.5, 4)`.
4. Sprawdź, że po poprawieniu `Prostokat` sama `Figura` nadal nie pozwala utworzyć instancji.

**Wyniki pól:** `12`, `0`, `10.0`. Wymiary są nieujemnymi liczbami, bez odczytu z klawiatury.  
**Wskazówka:** poprawna nazwa metody to dokładnie `pole`, zgodnie z bazą.

## Zadanie 3. Różne figury w jednym raporcie

1. Utwórz `Trojkat(Figura)`. Konstruktor przyjmuje nieujemną podstawę `a` i wysokość `h`. `pole()` zwraca `a * h / 2`.
2. Napisz funkcję `suma_pol(figury)`, która w jednej klasycznej pętli dodaje wyniki `figura.pole()` i zwraca sumę. Funkcja nie rozgałęzia działania według typu figury.
3. Wyświetl pola i sumę dla `[Prostokat(3, 4), Trojkat(4, 3), Prostokat(0, 5)]`.
4. Sprawdź pustą listę i listę z jednym trójkątem.

**Dane i wyniki:**

| Dane | Pola w kolejności | Suma |
|---|---|---|
| Trzy figury z polecenia | `12`, `6.0`, `0` | `18.0` |
| `[]` | brak elementów | `0` |
| `[Trojkat(4, 3)]` | `6.0` | `6.0` |
| `[Trojkat(0, 3)]` | `0.0` | `0.0` |

**Wskazówka:** zacznij od `suma = 0`, a w pętli użyj `suma += figura.pole()`.

## Zadanie 4. Dwa rodzaje pytań do quizu

Klasa bazowa jest gotowym szkieletem. `sprawdz(odpowiedz)` ma zwracać `bool`. Przyjmujemy wyłącznie napisy jako odpowiedzi, a klucz poprawnej odpowiedzi jest poprawny dla danego rodzaju pytania.

```python
from abc import ABC, abstractmethod

class Pytanie(ABC):
    def __init__(self, tresc, poprawna):
        self.tresc = tresc
        self.poprawna = poprawna

    @abstractmethod
    def sprawdz(self, odpowiedz):
        pass
```

1. Dodaj `PytanieTekstowe(Pytanie)`. Porównuje odpowiedź i klucz po usunięciu białych znaków z końców i bez rozróżniania wielkości liter: `strip().lower()`. Nie usuwamy spacji ze środka napisu.
2. Dodaj `PytanieWyboru(Pytanie)`. Dopuszcza jedną literę `A`, `B`, `C` lub `D`, z ignorowaniem wielkości liter i białych znaków z końców. Inna wartość daje `False`. Poprawny klucz jest jedną z liter A-D.
3. Obie klasy dziedziczą gotowe `__init__`. Nie definiuj kolejnego konstruktora, jeśli nie potrzebujesz nowych atrybutów.
4. Funkcja `policz_poprawne(proby)` przyjmuje listę par `(obiekt_pytania, odpowiedz)`. Jedną pętlą wywołuje `pytanie.sprawdz(odpowiedz)` i zwraca liczbę poprawnych odpowiedzi. Bez gałęzi zależnych od rodzaju pytania.
5. Wyświetl `tresc` obu pytań, wyniki pojedynczych prób oraz wynik funkcji dla listy prób i pustej listy.

**Dane:**

```python
tekstowe = PytanieTekstowe("Język tej lekcji?", "Python")
wyboru = PytanieWyboru("Która litera jest poprawna?", "B")
proby = [
    (tekstowe, " PYTHON "),
    (wyboru, " b "),
    (wyboru, "E"),
    (tekstowe, ""),
]
```

**Wyniki prób:** `True`, `True`, `False`, `False`; liczba poprawnych `2`; dla pustej listy `0`. Dodatkowo sprawdź `wyboru.sprawdz("BB")` → `False` i `tekstowe.sprawdz("Py thon")` → `False`.

## Zadanie 5. Dla chętnych: Walidacja wymiarów

Rozbuduj `Prostokat` i `Trojkat`, aby w konstruktorze zgłaszały `ValueError`, jeśli którykolwiek wymiar jest ujemny. Zero jest poprawne. Zachowaj dotychczasowe metody i funkcję `suma_pol`.

**Testy:** `Prostokat(-1, 4)` i `Trojkat(4, -2)` dają `ValueError`; `Prostokat(0, 4).pole()` daje `0`; `Trojkat(4, 0).pole()` daje `0.0`. Nie musisz obsługiwać napisów i `None`; zakres danych to liczby.  
**Przypomnienie:** `raise ValueError("Wymiary nie mogą być ujemne")` przerywa inicjalizację. Do pokazu oczekiwanego błędu użyj krótkiego `try/except ValueError`.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
