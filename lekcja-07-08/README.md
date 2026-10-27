# Ćwiczenia: Powtarzanie operacji: pętle for oraz while, przerywanie i wznawianie pętli

**Temat 4 | Lekcje 7-8**

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

## Zadanie 1

1. Pobierz liczbę całkowitą n. Gdy jest poza zakresem 1-10, wypisz „Błędny zakres” i pomiń obliczenia.
2. Dla poprawnego n wypisz w jednej linii liczby nieparzyste od 1 do n, włącznie.
3. Oblicz ich sumę w pętli i wypisz „Suma: …”. Nie używaj sum().
4. W osobnej linii wypisz odliczanie od n do 1, wykorzystując ujemny krok range().

Plik: zadanie1.py. Liczby w jednej linii oddziel spacją.

| Wejście n | Oczekiwane wyjście |
| --- | --- |
| 5 | Nieparzyste: 1 3 5<br>Suma: 9<br>Odliczanie: 5 4 3 2 1 |
| 1 | Nieparzyste: 1<br>Suma: 1<br>Odliczanie: 1 |
| 0 lub 11 | Błędny zakres |

Etykiety „Nieparzyste:” i „Odliczanie:” rozpocznij przed odpowiednią pętlą.

## Zadanie 2

1. Poprawny PIN to napis "0419". Użytkownik ma 3 próby na niepuste wpisy.
2. Pusty wpis po samym Enter: wypisz „Pusty PIN” i ponów pytanie przez continue bez utraty próby.
3. Poprawny PIN: ustaw flagę sukcesu, wypisz „Dostęp przyznany” i zakończ pętlę przez break.
4. Inny niepusty wpis zużywa próbę. Wypisz „Pozostało prób: …”. Po trzecim błędzie wypisz „Brak dostępu”.

Plik: zadanie2.py. Każdy niepusty wpis różny od "0419" jest błędną próbą.

| Kolejne wpisy | Oczekiwane komunikaty (skrót) |
| --- | --- |
| 0419 | Dostęp przyznany |
| Enter, 1111, 0419 | Pusty PIN / Pozostało prób: 2<br>Dostęp przyznany |
| 1111, 2222, 3333 | Pozostało prób: 2, potem 1, potem 0<br>Brak dostępu |
| 1111, 2222, 0419 | Pozostało prób: 2, potem 1<br>Dostęp przyznany |

Każdy komunikat wypisz w osobnej linii. PIN przechowuj jako tekst z zerem na początku.

To ćwiczenie autorskie na podstawie wcześniejszej symulacji z materiałów projektu, bez rzeczywistych kont i obsługi wypłat. Po sukcesie nie pytamy ponownie o PIN. Nie wymagamy kontroli długości PIN-u: każde niepuste wejście inne niż dokładnie `0419` zużywa próbę.

## Zadanie 3

1. Wczytuj temperatury jako liczby całkowite. Wartość 999 kończy serię przez break i nie trafia do raportu.
2. Przyjmuj wartości od -50 do 60, włącznie. Inne pomiń przez continue, wypisując „Odrzucono pomiar”.
3. Dla przyjętych danych oblicz licznik, sumę, minimum i maksimum, bez list oraz sum(), min() i max().
4. Jeżeli nie ma danych, wypisz „Brak danych”. W przeciwnym razie wypisz raport według poniższej tabeli.

Plik: zadanie3.py. Pierwszy przyjęty pomiar ustala minimum i maksimum.

| Pole raportu | 18, 150, 22, 14, 999 | -50, 60, 999 |
| --- | --- | --- |
| Liczba: | 3 | 2 |
| Suma: | 54 | 10 |
| Minimum: | 14 | -50 |
| Maksimum: | 22 | 60 |
| Średnia: | 18.00 | 5.00 |

150: Odrzucono pomiar. Samo 999: Brak danych. Każde pole raportu wypisz w osobnej linii.

Adaptacja analizatora temperatur z materiałów projektu do poznanych konstrukcji. Używamy całkowitych temperatur i jednego wartownika. To zadanie autorskie, nie wskazany arkusz CKE.

## Zadanie 4

1. Pobierz dwie liczby całkowite a i b. Gdy którakolwiek jest niedodatnia, wypisz „Liczby muszą być dodatnie”.
2. Dla poprawnych danych powtarzaj działania, dopóki a != b.
3. Jeśli a > b, zastąp a przez a - b. W przeciwnym przypadku zastąp b przez b - a.
4. Po pętli wypisz „NWD: …”. Dodatkowo policz iteracje i wypisz „Iteracje: …”.

Plik: zadanie4.py. Licznik iteracji jest rozszerzeniem szkolnym.

| a, b | Oczekiwane wyjście |
| --- | --- |
| 12, 8 | NWD: 4<br>Iteracje: 2 |
| 21, 15 | NWD: 3<br>Iteracje: 4 |
| 6, 6 | NWD: 6<br>Iteracje: 0 |
| 7, 1 | NWD: 1<br>Iteracje: 6 |
| 0, 8 lub -2, 8 | Liczby muszą być dodatnie |

Dla równych danych pętla nie wykona się ani razu.

**Źródło i adaptacja:** INF.04-01-23.01-SG, styczeń 2023, zadanie 1, część I. Oryginał wymaga funkcji NWD z dwoma argumentami, zwracającej wynik, bez operacji wejścia/wyjścia w jej wnętrzu. Dziś ćwiczymy sam algorytm w programie głównym i dodajemy licznik iteracji. Dokumentacja, pakowanie projektu i część desktopowa nie należą do tego ćwiczenia. W późniejszych tematach o funkcjach można wrócić do tego samego problemu i uzupełnić strukturę programu.

| Krok | a | b | Działanie |
|---|---|---|---|
| Start | 12 | 8 | a != b |
| 1 | 4 | 8 | a = 12 - 8 |
| 2 | 4 | 4 | b = 8 - 4 |
| Koniec | 4 | 4 | NWD = 4 |

## Zadanie 5 dla chętnych: tabliczka mnożenia

Pobierz n od 1 do 10. Przy błędnym zakresie wypisz „Błędny zakres”. Dla poprawnego n utwórz tabliczkę n × n przez dwie pętle `for`. Wypisuj iloczyny w polu szerokości 4 znaków, wyrównane do prawej. Po każdym wierszu przejdź do nowej linii.

Dla n = 3:

```text
   1   2   3
   2   4   6
   3   6   9
```

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
