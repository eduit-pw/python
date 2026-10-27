# Ćwiczenia: Ukrywanie wewnętrznych danych obiektu oraz bezpieczny dostęp za pomocą właściwości (@property)

**Temat 17 | Lekcje 33-34**

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

## Zadanie 1. Licznik z kontrolowaną zmianą

Zadanie autorskie. Napisz od początku `Licznik`:

1. Utwórz w konstruktorze `__wartosc = 0`.
2. Dodaj `pobierz_wartosc()` zwracające wartość oraz `zwieksz()` zwiększające ją o 1, bez jawnego zwracania wyniku.
3. Utwórz dwa liczniki. Pierwszy zwiększ dwukrotnie, drugi raz.
4. Wyświetl wartości przez metodę pobierającą. Nie zapisuj do pola z programu głównego.

**Oczekiwane wyniki:** przed zmianami `0 0`, po zmianach `2 1`. Wyjaśnij, dlaczego obiekty mają różne wartości.

## Zadanie 2. Cena przez właściwość

Zadanie autorskie. Zbuduj `Produkt(cena)` z właściwością `cena`:

1. Wewnętrzne `_cena` zaczyna od 0; argument konstruktora przechodzi przez setter.
2. Getter zwraca aktualną cenę. Setter zapisuje wyłącznie całkowite wartości 0-1000. Inne liczby całkowite pozostawiają dotychczasowy stan.
3. Utwórz produkt z ceną 40 i sprawdź przypisania z tabeli w podanej kolejności.
4. Osobno utwórz `Produkt(-1)` i `Produkt(1001)`. Oba mają cenę 0.

| Operacja na pierwszym produkcie | Cena po operacji |
|---|---|
| Utworzenie z 40 | 40 |
| Przypisanie 0 | 0 |
| Przypisanie 1000 | 1000 |
| Przypisanie -1 | 1000 |
| Przypisanie 1001 | 1000 |
| Przypisanie 25 | 25 |

## Zadanie 3. Liczba wypożyczeń tylko do odczytu

Zadanie autorskie. Napisz klasę `Egzemplarz`:

1. Konstruktor ustawia `_liczba_wypozyczen = 0`.
2. Właściwość `liczba_wypozyczen` ma getter i nie ma settera.
3. `wypozycz()` zwiększa wewnętrzny licznik o 1 i nie zwraca wyniku.
4. Utwórz dwa egzemplarze. Pierwszy wypożycz dwukrotnie, drugi pozostaw bez zmian. Odczytaj ich właściwości: oczekiwane wartości `2 0`.
5. W osobnej próbie sprawdź `egzemplarz.liczba_wypozyczen = 99`. Zapis ma zakończyć się `AttributeError`. Usuń tę próbę z normalnie uruchamianego programu.

Przez „tylko do odczytu” rozumiemy tutaj publiczną właściwość. Metoda klasy nadal może aktualizować wewnętrzny stan. Bezpośrednia zmiana `_liczba_wypozyczen` z zewnątrz jest technicznie możliwa, ale omija zaprojektowany interfejs.

## Zadanie 4. Wypożyczalnia filmów i dokumentacja

**Adaptacja CKE:** INF.04-03-23.06-SG, część I i dokumentacja części konsolowej z III. Polecenie w skrócie:

1. Zdefiniuj `Film`. Pola `_tytul` i `_liczba_wypozyczen` inicjalizuj jako `""` oraz `0`. Jeden podkreślnik odpowiada konwencji wymaganej w tym kluczu.
2. Napisz `ustaw_tytul(tytul)`, `pobierz_tytul()` i `pobierz_liczbe_wypozyczen()`.
3. Dodaj bezargumentowe `inkrementuj()`, które zwiększa liczbę wypożyczeń o 1 i nie zwraca wyniku.
4. W programie głównym utwórz obiekt, pokaż oba pola przez gettery, ustaw tytuł i pokaż stan ponownie. Wyświetl licznik przed inkrementacją i po niej.
5. Udokumentuj klasę komentarzem, uruchom program i przygotuj pliki opisane poniżej.

**Dane szkolnej próby:** tytuł `"Matrix"`, jedna inkrementacja. Dla tej lekcji przyjmujemy tytuły mające do 20 znaków. Arkusz dopuszcza to uproszczenie; nie określa reakcji na dłuższy tytuł. Nie dodawaj obcinania ani odrzucania danych jako rzekomego obowiązku egzaminacyjnego.

| Moment | Tytuł | Liczba wypożyczeń |
|---|---|---|
| Po konstruktorze | pusty napis | 0 |
| Po ustawieniu tytułu | Matrix | 0 |
| Po inkrementacji | Matrix | 1 |

**Dokumentacja i oddanie szkolnej adaptacji:**

- Nad klasą umieść komentarz opisujący nazwę klasy, pola, metody z wynikami, przeznaczenie klasy i szkolny numer autora. Użyj komentarzy `#`, nie samego docstringa.
- W folderze `konsola` pozostaw `main.py` i archiwum projektu `konsola.zip`.
- W folderze `dokumentacja` umieść pełny zrzut `konsola1.png`: widoczny wynik, środowisko pracy i pasek zadań.
- Utwórz dokument `egzamin.docx` lub `egzamin.odt` z podpisanym zrzutem, nazwą systemu, środowiska i języka. Jest to dokumentacja jedynie realizowanej części konsolowej.

Nie wymagamy osobnej metody wyświetlającej stan ani settera licznika. Nie trzeba używać `input()`: oryginał przewiduje test ustawienia dowolnego tytułu. Przygotowanie części webowej należy do osobnych zajęć.

## Zadanie 5. Dla chętnych: Ocena z walidacją - dodatkowe

Zadanie autorskie. Napisz `Uczen(ocena)` z właściwością `ocena`. Wewnętrzne `_ocena` zaczyna od 1. Setter przyjmuje liczby całkowite 1-6, a pozostałe liczby całkowite ignoruje. Konstruktor korzysta z tej samej reguły.

Testy: stan `Uczen(4)` to 4; przypisania kolejno 6, 0, 7, 1 dają stany 6, 6, 6, 1. `Uczen(0)` ma 1. Drugi uczeń pozostaje niezależny. Bez dodatkowej walidacji typów.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
