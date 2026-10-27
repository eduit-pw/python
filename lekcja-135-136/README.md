# Ćwiczenia: Rejestrowanie pracy programu: zapisywanie komunikatów, ostrzeżeń i błędów do pliku dziennika (logging)

**Temat 65 | Lekcje 135-136**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Ustalenia dziennika

Utwórz main.py. Konfigurację logging wykonaj raz, przed przetwarzaniem. Format wiersza ma zawierać datę i czas, poziom oraz wiadomość. Użyj trybu dopisywania, UTF-8 i loggera modułu. Przed pierwszą próbą zadania 1 zacznij od nowego pliku; kolejne uruchomienie ma dopisywać. Zadanie 2 zapisuje do osobnych nowych plików, aby nie mieszać liczników wpisów. W zadaniu 3 wybierz jedną strategię: WARNING z numerem wiersza bez traceback albo ERROR z traceback. Jeden błędny wiersz daje jedno zdarzenie. Próbę duplikacji handlerów wykonaj w osobnym programie i oddzielnym logu.

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

## Zadanie 1. Plik i dwa uruchomienia

- Skonfiguruj zapis UTF-8 do aplikacja.log na poziomie INFO.
- Zapisz START oraz KONIEC i uruchom program dwa razy.
- Sprawdź, że komunikaty z pierwszego uruchomienia pozostały.

**Wynik kontrolny:** łącznie 4 wpisy, bez nadpisania poprzednich.

## Zadanie 2. Próg poziomu

- Wyemituj po jednym komunikacie DEBUG, INFO, WARNING i ERROR.
- Uruchom osobno z progiem INFO i z progiem ERROR, w nowych plikach logów.

**Wynik kontrolny:** 3 wpisy przy INFO i 1 przy ERROR.

## Zadanie 3. Import z błędem

- Przetwarzaj wiersze 4, abc i 7. Poprawne liczby sumuj, błędne pomijaj.
- Zapisz WARNING z numerem wiersza albo ERROR z traceback, według przyjętej umowy.
- Na końcu zapisz liczbę poprawnych danych i sumę.

**Wynik kontrolny:** 2 poprawne liczby, suma 11, jeden opis błędnego wiersza.

## Zadanie 4. Powielone wpisy

- W małym przykładzie dodaj dwa osobne handlery zapisujące do tego samego pliku.
- Wyślij jeden komunikat i sprawdź duplikat. Popraw konfigurację do jednego handlera.
- Nie uruchamiaj addHandler w pętli przetwarzania danych.

**Wynik kontrolny:** po poprawce jedno zdarzenie daje jeden wpis.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
