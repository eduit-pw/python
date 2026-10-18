# Ćwiczenia: Gotowy panel zarządzania danymi w Django oraz tworzenie i sprawdzanie formularzy

**Temat 54 | Lekcje 111-112**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Kontynuacja i zasady formularza

Kontynuuj kopię projektu szkola_web z tematu 53. Zachowaj model Film, listę /filmy/ i bazę; nie dodawaj ponownie Poranka, jeśli już istnieje. Utwórz lokalne konto przez `py manage.py createsuperuser`. W ModelForm użyj pola ChoiceField z pustym wyborem oraz wartościami 1-4. Oczyść tytuł przez strip i odrzuć pusty. Przed zapisem sprawdzaj form.is_valid. Obsługuj GET i POST, pokaż błędy formularza i po sukcesie zastosuj przekierowanie do listy. Zachowaj middleware CSRF i znacznik csrf_token w formularzu. Do próby POST bez tokenu użyj klienta HTTP z włączoną kontrolą CSRF albo żądania z narzędzi przeglądarki.

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

## Zadanie 4. Przekierowanie i CSRF

- Dodaj film, odśwież docelową stronę i sprawdź brak powtórnego zapisu.
- W narzędziach przeglądarki sprawdź ukryte pole csrfmiddlewaretoken.
- Usuń token z wysyłanego POST w narzędziu testowym i sprawdź odpowiedź.

**Wynik kontrolny:** odświeżenie nie duplikuje filmu, POST bez tokenu daje 403.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
