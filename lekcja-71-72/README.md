# Ćwiczenia: Szybkość działania programów: wyszukiwanie liniowe, wyszukiwanie w posortowanej liście oraz Metoda Bisekcji

**Temat 35 | Lekcje 71-72**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Umowy wyszukiwania

Zapisz osobne funkcje. Liniowe wyszukiwanie zwraca pierwszy pasujący indeks albo -1 wraz z liczbą porównań. Wartownik również zwraca pierwszy indeks albo -1, nie zmieniając wejścia. Wyszukiwanie binarne wymaga posortowanej rosnąco listy: lewy=0, prawy=len(dane)-1, środek=(lewy+prawy)//2; po porównaniu odrzuć połowę, przesuwając granicę poza środek. Dla braku zwróć -1. W bisekcji x²-2 wybieraj połówkę zachowującą zmianę znaku; zakończ po uzyskaniu szerokości <= 0.001.

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

**Podczas pracy:** korzystaj z [tabel składni i krótkich wzorców](SCIAGA.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Indeks i liczba porównań

- Rozbuduj liniowe wyszukiwanie: zwracaj (indeks, liczba_porownan).
- Dla szukaj 3, 9 i 8. Sprawdź także pustą listę.
- Licz jedno porównanie elementu z szukaną wartością na odwiedzoną pozycję.

**Wynik kontrolny:** (1,2), (-1,4), (0,1). Dla []: (-1,0).

## Zadanie 2. Wartownik

- Napisz funkcję szukaj_wartownik(dane, x) używającą kopii listy.
- W pętli sprawdzaj tylko zgodność elementu z x. Po pętli sprawdź indeks.
- Dla szukaj 7 i 5. Upewnij się, że wejściowa lista się nie zmieniła. Adaptacja INF.04-01-22.06-SG, I: trzy własne wartości.

**Wynik kontrolny:** 1 i -1. Lista nadal.

## Zadanie 3. Wyszukiwanie binarne

- Napisz funkcję dla rosnącej listy.
- Sprawdź 12, 2, 14 i 5 oraz pustą listę.
- Wypisz badane indeksy dla szukania 12. Nie sortuj wewnątrz funkcji.

**Wynik kontrolny:** indeksy 5, 0, 6, -1. Dla []: -1. Badane: 3 i 5.

## Zadanie 4. Przybliżenie pierwiastka z 2

- Dla f(x)=x²-2 wykonaj bisekcję na, aż b-a <= 0.001.
- Zwróć środek ostatniego przedziału. Nie używaj sqrt do obliczeń.
- Policz iteracje i wypisz wynik z trzema miejscami po przecinku.

**Wynik kontrolny:** 10 iteracji, zapis 1.415. Przed zaokrągleniem błąd <= 0.0005.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
