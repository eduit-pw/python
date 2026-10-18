# Ćwiczenia: Działania na liczbach: sprawdzanie liczb pierwszych, Sito Eratostenesa, rozkład na czynniki i Algorytm Euklidesa

**Temat 33 | Lekcje 67-68**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Umowy algorytmów

`pierwsza(n)` zwraca bool: dla n < 2 wynik False. Szukaj dzielnika od 2, dopóki d*d <= n. `wypelnij(tablica)` modyfikuje tablicę sita: od p=2, przy zaznaczonym p wykreślaj wielokrotności od p*p do końca tablicy, następnie zwiększ p; kontynuuj, dopóki p*p mieści się w tablicy. Nie zwracaj nowej tablicy. Przy rozkładzie powtarzaj dzielenie przez d, dopóki reszta jest zerowa; na końcu uwzględnij pozostały czynnik > 1. NWD z odejmowaniem zapisuj w osobnej funkcji dla dodatnich argumentów.

## Zadanie 1. Przedział liczb pierwszych

- Napisz program wypisujący liczby pierwsze z przedziału 0-20.
- Użyj funkcji pierwsza i sprawdź osobno -7, 0, 1, 2, 49.
- Wyjaśnij, dlaczego warunek d*d <= n nie może być zastąpiony przez <.

**Wynik kontrolny:** 2, 3, 5, 7, 11, 13, 17, 19.

## Zadanie 2. Sito do 100

- Utwórz tablicę 101 wartości logicznych. Ustaw 0 i 1 na False.
- Napisz funkcję wypelnij(tablica) bez wartości zwracanej, zgodną z opisem algorytmu powyżej.
- Wypisz liczby pierwsze od 2 do 100 i ich liczbę. Adaptacja INF.04-01-23.06-SG, I: dodatkowe zliczanie wyników.

**Wynik kontrolny:** 25 liczb. Pierwsza 2, ostatnia 97.

## Zadanie 3. Rozkład i odtworzenie

- Napisz funkcję czynniki(n), przyjmującą int >= 2.
- Sprawdź 84, 49 i 13. Wypisz listę czynników i ich iloczyn.
- Odrzuć n < 2 przez ValueError.

**Wynik kontrolny:**,, [13]. Iloczyny: 84, 49, 13.

## Zadanie 4. NWD zgodnie z poleceniem

- Wczytaj dwie dodatnie liczby całkowite i oblicz NWD przez odejmowanie.
- Sprawdź pary (18,12), (7,5), (6,6). Odrzuć 0 i liczby ujemne.
- Porównaj wyniki z wersją modulo, używaną tylko jako kontrola. Adaptacja INF.04-01-23.01-SG, I: dodatnie dane i porównanie wersji.

**Wynik kontrolny:** 6, 1, 6.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
