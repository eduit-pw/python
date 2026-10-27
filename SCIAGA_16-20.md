# Python. Ściąga do tematów 16-20

| Zapis | Wywołany mechanizm / wynik |
| --- | --- |
| `str(x)`, `print(x)` | `x.__str__()` ma zwracać str. |
| `repr(x)`, elementy listy na wydruku | `x.__repr__()` daje opis diagnostyczny. |
| `len(x)` | `x.__len__()` zwraca nieujemną liczbę całkowitą. |
| `a == b` | protokół porównania `__eq__`; `is` bada tożsamość. |
| `p.cena` / `p.cena = 12` | getter / setter właściwości; bez nawiasów wywołania. |
| `super().metoda()` | następna implementacja w porządku wyszukiwania metod. |
| `iter(x)` / `next(it)` | iterator / kolejny element lub StopIteration. |
| `yield x` | oddanie elementu z możliwością wznowienia funkcji. |

## Temat 16

### __str__

str(obj) i print(obj) korzystają z __str__. Metoda zwraca str z opisem dla użytkownika. Nie umieszczaj w niej samego print, bo jego wynik None nie spełnia kontraktu.

### __repr__

repr(obj) daje reprezentację do analizy. Lista obiektów używa repr swoich elementów. !r we f-stringu również pobiera repr i poprawnie reprezentuje argument napisowy.

### __len__

len(obj) wywołuje __len__, które ma zwrócić nieujemny int. Dla własnej kolekcji zwykle zwracasz długość jej listy wewnętrznej, także 0.

### __eq__ i is

== korzysta z porównania wartości, które możesz zdefiniować w __eq__. is sprawdza tożsamość. Równe współrzędne nie oznaczają tego samego obiektu.

### NotImplemented

Dla nieobsługiwanego typu argumentu __eq__ może zwrócić NotImplemented. Jest to specjalna wartość, a nie wyjątek NotImplementedError. Python może wtedy spróbować drugiego porównania.

### Mały działający przykład

```python
class Punkt:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Punkt({self.x!r}, {self.y!r})"

    def __eq__(self, drugi):
        if not isinstance(drugi, Punkt):
            return NotImplemented
        return self.x == drugi.x and self.y == drugi.y

a, b = Punkt(2, 3), Punkt(2, 3)
print(a)              # (2, 3)
print([a])            # [Punkt(2, 3)]
print(a == b, a is b)  # True False
```

[Ćwiczenia](lekcja-31-32/README.md)

## Temat 17

### Hermetyzacja

Obiekt udostępnia kontrolowane operacje zamiast dowolnego zmieniania stanu przez kod zewnętrzny. W Pythonie _nazwa jest konwencją. __nazwa uruchamia zmianę nazwy związaną z klasą, a nie pełne zabezpieczenie danych.

### @property

Getter property pozwala czytać obj.cena bez nawiasów i wykonywać przy tym metodę. Powinien zwrócić pole pomocnicze, np. self._cena.

### Setter

@cena.setter obsługuje przypisanie obj.cena = wartosc. Wykonaj sprawdzenia przed zmianą pola. Reakcję na zły zakres określa zadanie: może to być ignorowanie albo wyjątek.

### Inicjalizacja przez setter

Jeśli konstruktor użyje self.cena = cena, zadziała ta sama reguła walidacji. W zadaniu z ignorowaniem błędu ustaw najpierw bezpieczną wartość początkową.

### Rekursja i tylko odczyt

self.cena wewnątrz gettera cena wywoła go ponownie. W setterze to samo zrobi przypisanie do self.cena. Korzystaj z _cena. Property bez settera blokuje przypisanie przez tę właściwość.

### Mały działający przykład

```python
class Produkt:
    def __init__(self, cena):
        self._cena = 0
        self.cena = cena

    @property
    def cena(self):
        return self._cena

    @cena.setter
    def cena(self, nowa):
        if nowa >= 0:
            self._cena = nowa

p = Produkt(10)
p.cena = -3
print(p.cena)  # 10; umowa przykładu: odrzucona zmiana zachowuje stan
p.cena = 12
print(p.cena)  # 12
```

[Ćwiczenia](lekcja-33-34/README.md)

## Temat 18

### Klasa bazowa i pochodna

class Pralka(Urzadzenie) tworzy klasę pochodną. Obiekt dziedziczy dostępne metody bazy. Dziedziczenie opisuje relację, w której obiekt pochodny jest rodzajem obiektu bazowego.

### Odziedziczone __init__

Klasa bez własnego __init__ może korzystać z inicjalizacji odziedziczonej. Definicja własnego __init__ zastępuje odziedziczone wywołanie, więc inicjalizację bazy trzeba świadomie uruchomić.

### super

super().__init__(nazwa) wykorzystuje dalszą inicjalizację w kolejności dziedziczenia. W prostym pojedynczym dziedziczeniu jest to baza. Nie przekazuj self drugi raz.

### Nadpisanie metody

Metoda o tej samej nazwie w klasie pochodnej nadpisuje zachowanie odziedziczone. super().opis() pozwala wykorzystać opis bazy i dopisać własne informacje.

### Spójność stanu

Po nieudanej zmianie programu pralki poprzednia wartość powinna pozostać. Sprawdź granice i dwa niezależne obiekty. self.opis() wewnątrz opis może wywoływać metodę rekurencyjnie.

### Mały działający przykład

```python
class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def opis(self):
        return self.imie

class Uczen(Osoba):
    def __init__(self, imie, klasa):
        super().__init__(imie)
        self.klasa = klasa

    def opis(self):
        return super().opis() + ", klasa " + self.klasa

print(Uczen("Ala", "2P").opis())  # Ala, klasa 2P
```

[Ćwiczenia](lekcja-35-36/README.md)

## Temat 19

### Polimorfizm

Ta sama operacja obj.pole() może działać inaczej dla prostokąta i trójkąta. Wspólna pętla korzysta z interfejsu bez sprawdzania typu każdego obiektu.

### Duck typing

Python może obsługiwać różne obiekty o zgodnym zachowaniu także bez wspólnej bazy. Ważne, aby używana metoda istniała i miała odpowiedni kontrakt.

### ABC i metoda abstrakcyjna

Dziedziczenie po ABC i @abstractmethod jawnie określa wymagania. Nie utworzysz instancji klasy z niezaimplementowanymi metodami abstrakcyjnymi.

### Kontrakt metody

Jeśli pole ma zwracać liczbę, wszystkie figury muszą zwracać liczbę. Sam print daje None i uniemożliwia sumowanie. Zachowaj sposób wywołania metody w podklasach.

### Normalizacja odpowiedzi

strip usuwa skrajne białe znaki, lower lub upper ujednolica litery. Nie usuwaj spacji wewnętrznych, gdy polecenie wymaga dokładnego tekstu. Sprawdź puste i niedozwolone odpowiedzi.

### Mały działający przykład

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass

class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok ** 2

class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return 3.14159 * self.promien ** 2

for figura in [Kwadrat(3), Kolo(1)]:
    print(figura.pole())  # 9, potem 3.14159
# Figura() zgłosi TypeError, bo pole pozostaje abstrakcyjne.
```

[Ćwiczenia](lekcja-37-38/README.md)

## Temat 20

### Iterable i iterator

iter(obiekt) pobiera iterator. next(iterator) zwraca następny element. Lista pozwala tworzyć nowe iteratory, a istniejący iterator pamięta bieżącą pozycję.

### Koniec iteracji

__next__ zgłasza StopIteration po wyczerpaniu. Pętla for obsługuje ten sygnał. next(it, domyslna) zwraca podaną wartość zamiast wyjątku, gdy iterator się skończył.

### Generator i yield

Wywołanie funkcji z yield tworzy generator. Kod zaczyna działać przy pobieraniu. yield oddaje wartość i wstrzymuje wykonanie z zachowaniem stanu. Kolejne pobranie wznawia kod za yield.

### Jednorazowość

Wyczerpany generator nie zaczyna od nowa. list(g) zużywa pozostałe elementy i przechowuje je w pamięci. sum(g), a potem kolejne przejście po g nie odczyta tych samych danych.

### Zużycie pamięci

Generator może uniknąć list wyników pośrednich. Nadal przechowuje swój stan i referencje do źródeł. Nie oznacza zerowego zużycia pamięci ani automatycznego zwolnienia całej listy wejściowej.

### Mały działający przykład

```python
def parzyste(dane):
    for x in dane:
        if x % 2 == 0:
            yield x

g = parzyste([1, 2, 3, 4])
print(next(g))        # 2
print(list(g))        # [4], tylko pozostałe elementy
print(list(g))        # [], generator już zużyty
print(next(g, None))  # None zamiast StopIteration
# Nowe wywołanie tworzy nowy generator:
print(list(parzyste([1, 2, 3, 4])))  # [2, 4]
```

[Ćwiczenia](lekcja-39-40/README.md)

## Szybka kontrola przed oddaniem

- Czy `__str__` zwraca napis, a nie wynik print?
- Czy `__len__` nie wywołuje ponownie len(self)?
- Czy właściwość używa osobnego pola, np. _cena?
- Czy konstruktor potomny inicjalizuje wymagane dane bazowe?
- Czy każda klasa konkretna realizuje metody abstrakcyjne?
- Czy nie próbujesz drugi raz odczytać zużytego generatora?
