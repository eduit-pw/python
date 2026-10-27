# Ćwiczenia: Niemodyfikowalne krotki oraz działania na zbiorach: łączenie, część wspólna i usuwanie duplikatów

**Temat 9 | Lekcje 17-18**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

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

## Zadanie 1. Dwa punkty pomiarowe

Upraszczamy dane do liczb całkowitych; nie obliczamy odległości geograficznej ani nie wymagamy try/except. Pola punktu: (szerokosc, dlugosc, wysokosc, kod). Wysokość w metrach.

Dane: baza = (50, 19, 220, "STACJA-A"), cel = (51, 20, 285, "MASZT-B").

1. Napisz porownaj_punkty(baza, cel). Rozpakuj oba rekordy do nazwanych zmiennych.
2. Oblicz wysokość celu minus wysokość bazy; zwróć (kod_bazy, kod_celu, roznica).
3. Funkcja nie zmienia argumentów ani nie wypisuje. Program główny wypisuje wynik.
4. W programie głównym rozpakuj bazę, zamień zmienne szerokości i długości przez a, b = b, a, pokaż je i potwierdź, że baza pozostaje bez zmian.

| Argumenty | Wynik |
|---|---|
| baza, cel | ('STACJA-A', 'MASZT-B', 65) |
| cel, baza | ('MASZT-B', 'STACJA-A', -65) |
| baza, baza | ('STACJA-A', 'STACJA-A', 0) |

Przyjmujemy poprawne czteroelementowe krotki, trzy pola liczbowe i tekstowy kod. Nie wymagamy walidacji liczby pól. Zamiana zmiennych w celu demonstracji nie zmienia znaczenia danych w źródłowym rekordzie.

## Zadanie 2. Uprawnienia

Punkt wyjścia: projektowe ćwiczenie uprawnień, uproszczone do kilku nazw. To model danych do ćwiczenia zbiorów, bez integracji z rzeczywistym systemem logowania.

```python
user = {"login", "read"}
editor = user | {"write"}
admin = editor | {"delete"}
wymagane = {"read", "delete"}
```

1. Napisz sprawdz_uprawnienia(posiadane, wymagane).
2. Zwróć krotkę (czy_dopuszczony, brakujace): bool i nowy zbiór brakujących nazw operacji.
3. Zastosuj wymagane.issubset(posiadane) oraz wymagane - posiadane. Nie zmieniaj zbiorów wejściowych i nie wypisuj w funkcji.
4. W programie głównym zbadaj editor oraz admin, wypisz część wspólną trzech ról i admin - editor. Wyniki zbiorowe pokazuj przez sorted.

| Posiadane | Wymagane | Wynik |
|---|---|---|
| editor | {'read', 'delete'} | (False, {'delete'}) |
| admin | {'read', 'delete'} | (True, set()) |
| set() | set() | (True, set()) |
| set() | {'read'} | (False, {'read'}) |

Część wspólna trzech ról: {'login', 'read'}. Tylko admin względem editor: {'delete'}. Puste wymagania są spełnione niezależnie od posiadanych uprawnień. Ta własność matematyczna nie definiuje samodzielnie polityki bezpieczeństwa aplikacji.

## Zadanie 3. Dwie sesje logowań

Zastępujemy adresy IP prostymi loginami i pomijamy walidację IPv4, aby ćwiczyć kolekcje. To zadanie szkolne, nie kopia wskazanego arkusza CKE.

Dane: rano = [" ala ", "jan", "Ala", "ola", " "], popoludnie = ["Jan", "ewa", "ewa"].

1. Napisz oczysc_loginy(loginy). Dla każdego wpisu wykonaj strip().lower(); pomiń pusty wynik. Zwróć listę bez powtórzeń w kolejności pierwszych wystąpień, używając pętli, zbioru widzianych i listy wynikowej.
2. Napisz porownaj_sesje(rano, popoludnie), przyjmując już oczyszczone listy. Zamień je na zbiory.
3. Zwróć krotkę (wszyscy, wspolni, nowi) z trzema nowymi zbiorami. Nowi oznacza loginy z popołudnia nieobecne rano.
4. Funkcje nie zmieniają wejściowych list i nie wykonują input/print. Program główny wyświetla oczyszczone listy oraz posortowane wyniki zbiorowe.

| Wynik dla danych podstawowych | Oczekiwana wartość |
|---|---|
| Rano po oczyszczeniu | ['ala', 'jan', 'ola'] |
| Po południu po oczyszczeniu | ['jan', 'ewa'] |
| Wszyscy, po sorted | ['ala', 'ewa', 'jan', 'ola'] |
| Wspólni, po sorted | ['jan'] |
| Nowi, po sorted | ['ewa'] |

Testuj także dwie puste listy, listy samych odstępów i przypadek rano = ['ala'], popoludnie = []. Dla dwóch pustych wejść mamy dwie puste listy oraz trzy puste zbiory. Gdy rano jest ala, a po południu nic: wszyscy {'ala'}, wspolni set(), nowi set(). Nie wymagamy, by kolejność zbioru zgadzała się z wejściem. Normalizacja do małych liter jest regułą tego ćwiczenia, nie uniwersalną regułą każdego systemu kont.

## Zadanie 4. Sześć różnych liczb - przygotowanie do INF.04-01-25.06-SG

Projektowe § 1.6 opisuje loterię z sześcioma różnymi liczbami z zakresu 1-49. Z arkuszem i kluczem zweryfikowano warunki, a nie tylko skrót projektowy. **Z oryginału bierzemy rozmiar i zakres zestawu oraz brak powtórzeń.** Nasz wybór z gotowej listy nie jest losowaniem, dlatego nie przypisujemy mu spełnienia kryterium dotyczącego generatora lub losowania bez powtórzeń.

Dane: kandydaci = [0, 5, 5, 12, 49, 1, 7, 23, 50, 8], wygrane = (1, 7, 13, 23, 30, 49).

1. Napisz wybierz_zestaw(kandydaci). Przeglądaj listę od początku. Pomijaj liczby spoza 1-49 i liczby wcześniej wybrane.
2. Użyj zbioru widzianych oraz listy zachowującej kolejność. Po znalezieniu sześciu różnych liczb zwróć tuple(wynik) i zakończ funkcję. Gdy zabraknie takich liczb, zwróć None.
3. Napisz czy_poprawny_zestaw(zestaw), zwracającą bool: dokładnie 6 elementów, wszystkie różne i z zakresu 1-49.
4. Napisz trafienia(zestaw, wygrane), zwracającą set wspólnych liczb. To autorskie rozszerzenie szkolne, nie wymaganie tej loterii w arkuszu.
5. Program główny obsługuje None komunikatem. Dla krotki pokazuje kolejność wyboru, wersję posortowaną, wynik kontroli i posortowane trafienia wraz z ich liczbą.
6. Funkcje nie zmieniają wejścia, nie używają zmiennych globalnych i nie wykonują wejścia/wyjścia. Dodaj nagłówek wybranej funkcji oraz dokumentację uruchomienia.

Przyjmujemy całkowite elementy kandydatów. czy_poprawny_zestaw przyjmuje listę lub krotkę liczb całkowitych, nie None. trafienia otrzymuje dwa poprawne sześcioliczbowe zestawy. Program główny nie wywołuje tych funkcji dla None. Nie wymagamy walidacji typów; błędny zakres i duplikaty są sprawdzane jawnie.

| Próba | Oczekiwany wynik |
|---|---|
| wybierz_zestaw dla danych podstawowych | (5, 12, 49, 1, 7, 23) |
| Posortowany wybrany zestaw | [1, 5, 7, 12, 23, 49] |
| Trafienia dla danych podstawowych | {1, 7, 23, 49}, liczba 4 |
| Kandydaci [1, 2, 3, 4, 5, 6] | (1, 2, 3, 4, 5, 6) |
| Kandydaci [] lub [1, 1, 2, 3] | None |
| Kontrola (1, 2, 3, 4, 5, 49) | True |
| Kontrola (1, 2, 3, 4, 5, 5) | False |
| Kontrola (0, 2, 3, 4, 5, 6) | False |
| Kontrola (1, 2, 3, 4, 5, 50) | False |
| Kontrola (1, 2, 3, 4, 5) lub () | False |

Dodatkowo sprawdź trafienia bez wspólnych liczb i dla identycznych zestawów: odpowiednio set() oraz sześć liczb. Nie usuwaj powtórzeń z gotowego błędnego zestawu w funkcji kontroli, aby następnie uznać go za poprawny. Zadaniem tej funkcji jest sprawdzenie danych, nie ich naprawianie.

Pełna konsola z arkusza pobiera liczbę losowań, generuje wiele zestawów funkcją pseudolosową, przechowuje je, wyświetla i zlicza wystąpienia liczb 1-49. Nasz etap przygotowawczy nie zastępuje tych wymagań. Sortowanie raportu jest wyborem szkolnym: oryginał nie narzuca sortowania każdego zestawu jako osobnego wymogu. Zbiory nie zachowają liczby powtórzeń między losowaniami; nie wolno zastąpić całego rejestru losowań jednym set.

## Zadanie 5. Dla chętnych: Unikalne punkty - autorskie, dodatkowe

Dane: punkty = [(1, 2), (2, 3), (1, 2)]. Napisz unikalne_punkty(punkty). Każdy punkt jest krotką dwóch liczb całkowitych. Pętlą dodawaj je do zbioru, a potem zwróć krotkę (posortowana_lista, liczba_punktow). Funkcja nie zmienia wejścia i niczego nie wypisuje; wynik wyświetla program główny.

| Wejście | Wynik |
|---|---|
| [(1, 2), (2, 3), (1, 2)] | ([(1, 2), (2, 3)], 2) |
| [] | ([], 0) |
| [(1, 2), (2, 1)] | ([(1, 2), (2, 1)], 2) |

Kolejność wewnątrz punktu jest znacząca. sorted krotek porównuje najpierw pierwszą współrzędną, a przy równości kolejną. To rozszerzenie, nie wymagamy ogólnego wykładu o porządku leksykograficznym.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
