# Ćwiczenia: Podstawy programowania obiektowego: tworzenie klas, obiektów i konstruktora __init__

**Temat 14 | Lekcje 27-28**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Dwoje uczniów

1. Utwórz `Uczen(imie, klasa)` z polami `self.imie` i `self.klasa`.
2. Dodaj `przedstaw()`, zwracającą napis w formacie `Ala, klasa 3TP`.
3. Utwórz Alę z klasy 3TP i Jana z klasy 2TP. Wyświetl wyniki ich metod.
4. Zmień klasę Jana na 3TP i ponownie wyświetl opisy obu obiektów. Sprawdź, czy dane Ali pozostały bez zmian.

Oczekiwane opisy: przed zmianą `Ala, klasa 3TP`, `Jan, klasa 2TP`; po zmianie `Ala, klasa 3TP`, `Jan, klasa 3TP`. Dodatkowo utwórz trzeciego ucznia i sprawdź jego opis.

## Zadanie 2. Prostokąty

1. Utwórz `Prostokat(szerokosc, wysokosc)`. Wymiary są dodatnimi liczbami całkowitymi w centymetrach.
2. Dodaj `pole()` i `obwod()`, zwracające wyniki obliczone z aktualnych pól obiektu. Nie zapamiętuj obliczonego pola jako osobnego pola instancji.
3. Utwórz prostokąty 4 × 3 i 2 × 5. Wyświetl pole i obwód każdego.
4. Zmień szerokość pierwszego na 6. Ponownie oblicz oba wyniki i sprawdź, że drugi prostokąt zachował stan.

| Prostokąt / etap | Pole (cm²) | Obwód (cm) |
|---|---:|---:|
| 4 × 3 | 12 | 14 |
| 2 × 5 | 10 | 14 |
| Pierwszy po zmianie: 6 × 3 | 18 | 18 |
| Drugi po zmianie pierwszego | 10 | 14 |

Dodatkowo sprawdź kwadrat 5 × 5. Przyjmujemy poprawne dodatnie wymiary, bez walidacji.

## Zadanie 3. Dwa niezależne liczniki

1. Utwórz `Licznik()` z polem instancji `wartosc`, początkowo 0.
2. Dodaj `zwieksz()`, która zwiększa wartość o 1, i `wyzeruj()`, która ustawia 0. Obie metody zmieniają stan i nie zwracają danych.
3. Dodaj `pobierz()`, zwracającą aktualną wartość.
4. Utwórz dwa liczniki. Pierwszy zwiększ dwukrotnie, drugi jednokrotnie. Wyświetl oba, wyzeruj pierwszy i odczytaj je ponownie.

Oczekiwane pary: początkowo `0 0`, po zwiększeniach `2 1`, po zerowaniu `0 1`. Dodatkowo zwiększ ponownie pierwszy licznik i sprawdź parę `1 1`. To dwa pola instancji; wspólny licznik klasy pojawi się w temacie 15.

## Zadanie 4. Film w wypożyczalni

1. Utwórz `Film()` z początkowymi polami `_tytul = ""` oraz `_liczba_wypozyczen = 0`.
2. Dodaj `ustaw_tytul(tytul)`, `pobierz_tytul()` i `pobierz_liczbe_wypozyczen()`.
3. `wypozycz()` zwiększa licznik o 1 i nie zwraca danych.
4. W programie głównym pokaż stan początkowy, ustaw tytuł „Seksmisja”, odczytaj go oraz wyświetl licznik przed i po wypożyczeniu. Przygotuj dokumentację klasy i uruchomienia.

Nazwy metod i dane testowe dobrano szkolnie. Zachowujemy wymagane operacje. Pojedynczy podkreślnik odpowiada konwencji `protected` wskazanej w kluczu; nie blokuje technicznie dostępu. Poza klasą korzystamy z metod. Oryginał dopuszcza uproszczenie do 20 znaków tytułu, ale nie nakazuje walidacji długości. W tej wersji setter zwyczajnie przypisuje napis.

| Etap | Tytuł | Liczba wypożyczeń |
|---|---|---:|
| Utworzenie obiektu | `""` | 0 |
| Ustawienie tytułu | Seksmisja | 0 |
| Pierwsze wypożyczenie | Seksmisja | 1 |

Szkolne testy dodatkowe: drugie wypożyczenie daje 2; zmiana tytułu nie zeruje licznika; drugi, nowy film zaczyna od `""` i 0. `input()` nie jest wymagane przez tę część arkusza. Można użyć danych zapisanych w kodzie.

Wzór początkowej klasy:

```python
class Film:
    def __init__(self):
        self._tytul = ""
        self._liczba_wypozyczen = 0

    def pobierz_tytul(self):
        return self._tytul
```

## Zadanie 5. Dla chętnych: Lista obiektów (autorskie, opcjonalne)

Utwórz listę trzech obiektów `Uczen`. W pętli wyświetl wynik `przedstaw()` dla każdego ucznia. Zmień klasę drugiego ucznia przez indeks listy i ponownie wyświetl jego opis. Lista zawiera odwołania do obiektów; pobrany z niej uczeń nadal ma swoje pola i metody.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
