# Ćwiczenia: Tworzenie tabel bazy danych w Django za pomocą modeli i aktualizacja bazy (ORM)

**Temat 53 | Lekcje 109-110**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Model i dane początkowe

Kontynuuj kopię projektu szkola_web z poprzedniej lekcji. W `strony/models.py` zdefiniuj Film: tytul = CharField(max_length=80), rodzaj = PositiveSmallIntegerField(default=1), wypozyczenia = PositiveIntegerField(default=0). __str__ zwraca tytuł. Pole dostepny dodaj dopiero w zadaniu 4. Dane początkowe: Poranek i Wieczór, rodzaj=1, wypozyczenia=0. Pracuj na nowej bazie ćwiczeniowej i nie kasuj bazy poprzedniej lekcji. Twórz rekordy tylko raz.

```powershell
py manage.py makemigrations strony
py manage.py migrate
py manage.py shell
```

Po każdej zmianie modelu utwórz i zastosuj migrację. Serwer uruchamiaj przez `py manage.py runserver` z folderu zawierającego manage.py.

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

## Zadanie 1. Pierwsza tabela

- Dodaj model Film opisany powyżej, wykonaj makemigrations i migrate.
- W shell utwórz Poranek i Wieczór. Zacznij od nowej bazy ćwiczeniowej.
- Zamknij shell, otwórz go ponownie i odczytaj rekordy.

**Wynik kontrolny:** 2 rekordy po ponownym uruchomieniu.

## Zadanie 2. Zapytanie i sortowanie

- Dodaj film Alarm z rodzaj=3. Pozostałe dwa mają rodzaj=1.
- Pobierz tylko rodzaj=1 i posortuj tytuły rosnąco.
- Osobno sprawdź filter(pk=999).first(), zakładając brak tego ID.

**Wynik kontrolny:** Poranek, Wieczór oraz None dla brakującego ID.

## Zadanie 3. Lista na stronie

- Utwórz /filmy/ i szablon z tytułem oraz liczbą wypożyczeń każdego rekordu.
- Zmień liczbę wypożyczeń Poranka na 2 w shell i odśwież stronę.
- Dodaj obsługę pustej listy przez {% empty %}.

**Wynik kontrolny:** widok pokazuje stan zapisany w bazie.

## Zadanie 4. Zmiana schematu

- Dodaj pole dostepny = models.BooleanField(default=True). Utwórz i zastosuj migrację.
- Sprawdź poprzednie rekordy. Ustaw False tylko dla Alarmu i zapisz go.

**Wynik kontrolny:** stare dane pozostają, Alarm ma dostepny=False.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
