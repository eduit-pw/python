# Ćwiczenia: Gotowy panel zarządzania danymi w Django oraz tworzenie i sprawdzanie formularzy

**Temat 57 | Lekcje 113-114**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Kontynuacja i zasady formularza

Kontynuuj kopię projektu szkola_web z tematu 56. Zachowaj model Film, listę /filmy/ i bazę; nie dodawaj ponownie Poranka, jeśli już istnieje. Utwórz lokalne konto przez `py manage.py createsuperuser`. W ModelForm użyj pola ChoiceField z pustym wyborem oraz wartościami 1-4. Oczyść tytuł przez strip i odrzuć pusty. Przed zapisem wywołaj `form.is_valid()` i zapisuj dane tylko wtedy, gdy zwróci `True`. Obsługuj GET i POST, pokaż błędy formularza i po sukcesie zastosuj przekierowanie do listy. Zachowaj middleware CSRF i znacznik csrf_token w formularzu. Do próby POST bez tokenu użyj klienta HTTP z włączoną kontrolą CSRF albo żądania z narzędzi przeglądarki.

## Sposób pracy podczas bloku

| Etap | Czas | Co robisz |
| --- | ---: | --- |
| Wyjaśnienia i demonstracja | 0-25 min | Czytasz przykład, przewidujesz wynik i zadajesz pytania. |
| Zadanie 1 z prowadzącym | 25-35 min | Uruchamiasz pierwszy wariant i objaśniasz kluczowy zapis. |
| Zadanie 2 wspólnie | 35-50 min | Proponujesz kolejne kroki, sam zapisujesz kod. |
| Zadanie 3 samodzielnie | 50-70 min | Realizujesz kontrakt i wykonujesz próby. |
| Formularz bez modelu i funkcja | 70-82 min | Łączysz forms.Form ze wspólną logiką. |
| Zapis działającego etapu w Git | 82-85 min | Sprawdzasz różnicę i tworzysz commit. |
| Zakończenie | 85-90 min | Zapisujesz kod, jeden wniosek i wykonane próby. |

Zadanie 4 i diagnoza są dla chętnych lub do samodzielnej kontynuacji. W podstawowym bloku zachowaj czas na połączenie formularza z funkcją. Tempo ustala nauczyciel.

**Podczas pracy:** korzystaj z [tabel składni i krótkich wzorców](KONSTRUKCJE.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Dane w panelu admina

- Zarejestruj Film, utwórz lokalne konto admina i dodaj film Poranek, rodzaj=1.
- Wyszukaj go po tytule. Otwórz /filmy/ i porównaj wynik.

**Wynik kontrolny:** admin i widok pokazują ten sam rekord.

## Zadanie 2. Formularz filmu

- Utwórz ModelForm i stronę /filmy/dodaj/ z polami „Tytuł filmu” i „Rodzaj”.
- Rodzaje: pusta opcja, Komedia=1, Obyczajowy=2, Sensacyjny=3, Horror=4.
- Przycisk „Dodaj” zapisuje poprawny film i przekierowuje do listy. Adaptacja INF.04-03-23.06-SG, II: Django i zapis do bazy zamiast konsoli.

**Wynik kontrolny:** Alarm i rodzaj 3 tworzą dokładnie 1 rekord.

## Zadanie 3. Niepoprawne dane

- Wyślij formularz z pustym tytułem, samymi spacjami i bez wyboru rodzaju.
- Sprawdź komunikaty oraz liczbę rekordów przed i po każdym przypadku.

**Wynik kontrolny:** błędy są widoczne, liczba filmów nie zmienia się.

## Zadanie 4. Dla chętnych: Przekierowanie i CSRF

- Dodaj film, odśwież docelową stronę i sprawdź brak powtórnego zapisu.
- W narzędziach przeglądarki sprawdź ukryte pole csrfmiddlewaretoken.
- Usuń token z wysyłanego POST w narzędziu testowym i sprawdź odpowiedź.

**Wynik kontrolny:** odświeżenie nie duplikuje filmu, POST bez tokenu daje 403.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)

## Utrwalanie Git w ramach tego bloku

Przed zmianą sprawdź `git status`, a po działającej poprawce obejrzyj `git diff`. Zapisz mały commit z opisem wykonanej zmiany. Czynność zajmuje 2–3 minuty przewidziane na sprawdzenie pracy.

## Formularz obliczeniowy w ramach zadania 3

Ostatnie 10–12 minut podstawowej pracy przeznacz na prosty wariant bez modelu. `forms.Form` opisuje formularz bez zapisu w bazie. `IntegerField(min_value=0)` wymaga nieujemnej liczby całkowitej. W widoku utwórz formularz, sprawdź `is_valid()`, odczytaj `cleaned_data` i przekaż je do funkcji w osobnym module. Wynik pokaż w szablonie z formularzem i tokenem CSRF.

Przykład nauczycielski: pola `liczba` i `mnoznik`, funkcja zwracająca ich iloczyn. Sprawdź 7 i 2, zero oraz wartość ujemną. To trening łączenia znanych elementów, nie treść próby. Zakończ małym commitem działającej wersji.

Gotowy przykład: [formularz bez modelu](przyklady/formularz_bez_modelu/). Służy do demonstracji i zmiany danych w ostatniej części zadania 3.
