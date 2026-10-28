# Ćwiczenia: Sprawdzanie i zabezpieczanie przesyłanych danych w FastAPI za pomocą schematów Pydantic

**Temat 56 | Lekcje 115-116**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Umowa modeli

Kontynuuj kopię projektu z tematu 55. Użyj Pydantic 2. `AlbumWejscie` ma tytul: str z długością 1-80, walidator po strip odrzucający pusty wynik, oraz pobrania: int z ge=0 i strict=True. Początkowo pobrania jest wymagane. ConfigDict(extra="forbid") odrzuca dodatkowe pola. POST /sprawdz zwraca zwalidowane dane z kodem 200. `AlbumOdczyt` zawiera te same pola oraz id: int; POST /podglad zwraca dane wejścia i ustalone na potrzeby ćwiczenia id=7, z response_model=AlbumOdczyt. To podgląd bez zapisu i bez generowania kolejnych ID.

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

## Zadanie 1. Model i poprawny POST

- Dodaj AlbumWejscie, walidator tytułu i POST /sprawdz.
- Wyślij {"tytul":" Poranek ","pobrania":0} przez /docs.

**Wynik kontrolny:** 200, tytuł Poranek bez skrajnych spacji i liczba 0.

## Zadanie 2. Granice danych

- Sprawdź tytuł długości 80 i 81 znaków, pusty tekst oraz same spacje.
- Dla pobrania sprawdź 0, -1, "3" i true.
- Zapisz, które pole wskazuje detail w odpowiedzi 422.

**Wynik kontrolny:** 80 znaków i liczba 0 poprawne, pozostałe wymienione błędy odrzucone.

## Zadanie 3. Brakujące i dodatkowe pola

- Wyślij JSON bez pobrania, potem z pobrania=2 i dodatkowym id=99.
- Zmień deklarację pobrania na Field(default=0, ge=0, strict=True).
- Ponownie wyślij tylko tytul i porównaj wyniki.

**Wynik kontrolny:** początkowo 422, po zmianie brak pobrania przyjmuje 0; id nadal odrzucone.

## Zadanie 4. Wynik opisany schematem

- Dodaj AlbumOdczyt i POST /podglad zgodnie z umową powyżej.
- Wyślij poprawny album. Sprawdź schemat odpowiedzi w /docs.
- Wyjaśnij, kto nadaje id i dlaczego klient nie wysyła go w AlbumWejscie.

**Wynik kontrolny:** odpowiedź ma id=7 oraz oba pola albumu.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
