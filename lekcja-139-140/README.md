# Ćwiczenia: Współbieżne wykonywanie zadań i programowanie asynchroniczne: moduł asyncio oraz instrukcje async i await

**Temat 67 | Lekcje 139-140**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Symulacja operacji i pomiar czasu

Napisz `async def pobierz(nazwa, czas)`: zaczekaj przez await asyncio.sleep(czas), wypisz nazwę zakończonej operacji i zwróć nazwę. Nie korzystaj z zewnętrznej sieci. Wariant sekwencyjny wykonuje osobne await jedno po drugim; współbieżny używa asyncio.gather. Program uruchamiaj przez asyncio.run(main()), w zwykłym skrypcie main.py. Zmierz czas przez time.perf_counter. Czasy kontrolne są przybliżone i zależą od stanowiska.

W zadaniu 3 użyj `async with asyncio.timeout(0.1)`; except TimeoutError umieść poza tym blokiem, a po obsłudze wykonaj pobierz z czasem 0.01. Zadanie 4 wymaga dwóch osobnych wersji korutyny, jednej blokującej i drugiej nieblokującej.

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

## Zadanie 1. Sekwencja i współbieżność

- Uruchom pobierz dla A=0,3 s oraz B=0,5 s w wariancie sekwencyjnym i współbieżnym opisanym powyżej.
- Zmierz perf_counter przed i po operacji. Porównaj wyniki i czas.

**Wynik kontrolny:** te same dane; około 0,8 s sekwencyjnie i 0,5 s współbieżnie.

## Zadanie 2. Kolejność wyników

- Utwórz zadania A=0,5 s, B=0,1 s i C=0,3 s. Przekaż je do gather w kolejności A, B, C.
- Zapisz w korutynie chwilę zakończenia i porównaj ją z listą wyników.

**Wynik kontrolny:** B kończy pierwsze, wyniki gather to A, B, C.

## Zadanie 3. Przekroczenie czasu

- Zastosuj timeout=0,1 s do pobierz z czasem 0,5 s.
- Pokaż komunikat błędu, potem wykonaj osobną szybką operację.
- Nie umieszczaj except TimeoutError wewnątrz bloku timeout.

**Wynik kontrolny:** komunikat o czasie, a program nadal wykonuje kolejną operację.

## Zadanie 4. Blokujące i nieblokujące oczekiwanie

- W dwóch zadaniach porównaj time.sleep(0.3) z await asyncio.sleep(0.3).
- W obu wariantach zaplanuj zadania współbieżnie i zmierz czas.
- Wyjaśnij, dlaczego time.sleep blokuje postęp drugiego zadania.

**Wynik kontrolny:** około 0,6 s z time.sleep, około 0,3 s z asyncio.sleep.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
