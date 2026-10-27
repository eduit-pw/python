# Ćwiczenia: Dodawanie i obsługa elementów okna: napisy, pola tekstowe, przyciski i opcje wyboru

**Temat 41 | Lekcje 83-84**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Ustalenia formularza

Kod zapisuj w `main.py` albo w osobnych plikach kolejnych zadań. Wyniki pokaż jako tekst, np. przez QLabel.setText; nie interpretuj tekstu użytkownika jako HTML. Cennik do zadania 3: Pocztówka = 1 zł, List = 1,5 zł, Paczka = 10 zł. Początkowo wybrana jest Pocztówka, ale cena pojawia się po kliknięciu. W zadaniu 4 najpierw sprawdzaj długość kodu, potem każdy znak jako cyfrę ASCII 0-9; wynik wyświetlaj po kliknięciu „Zatwierdź”.

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

## Zadanie 1. Formularz ucznia

- Zbuduj QLineEdit „Imię”, QSpinBox 1-5 „Klasa” i przycisk „Pokaż”.
- Po kliknięciu wypisz w QLabel: „Anna, klasa 4” dla danych Anna i 4.
- Puste imię po strip ma dawać „Podaj imię”.

**Wynik kontrolny:** poprawne podsumowanie albo komunikat pustego pola.

## Zadanie 2. Opcje niezależne

- Dodaj QCheckBox „Python” i „SQL” oraz przycisk podsumowania.
- Wypisz wybrane nazwy w tej kolejności, rozdzielone przecinkiem.
- Gdy żadna nie jest wybrana, pokaż „Brak wyboru”.

**Wynik kontrolny:** „Python”, „SQL”, „Python, SQL” albo „Brak wyboru”.

## Zadanie 3. Rodzaj przesyłki i cena

- Utwórz trzy pola radio i QButtonGroup. Pocztówka wybrana na początku.
- Dodaj przycisk „Sprawdź cenę” i QLabel z początkowym tekstem „Cena:”.
- Wyświetl cenę z powyższego cennika. Obraz zastąp etykietą rodzaju przesyłki. Adaptacja INF.04-01-23.06-SG, II: etykieta zamiast obrazu.

**Wynik kontrolny:** List: 1,5 zł. Paczka: 10 zł.

## Zadanie 4. Kod i zatwierdzenie

- Do zadania 3 dodaj QLineEdit kodu oraz przycisk „Zatwierdź”.
- Za krótki lub długi kod: „Wymagane 5 znaków”. Obcy znak: „Wymagane cyfry”.
- Poprawny kod: „Dane poprawne”. Sprawdź 12345, 1234, 12a45 i 12-345. Adaptacja INF.04-01-23.06-SG, II: uproszczone komunikaty.

**Wynik kontrolny:** tylko 12345 daje potwierdzenie.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
