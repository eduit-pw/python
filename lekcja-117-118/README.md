# Ćwiczenia: Pełna obsługa danych w FastAPI: pobieranie, dodawanie, edycja i usuwanie wpisów przez sieć

**Temat 57 | Lekcje 117-118**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Kontrakt CRUD

Kontynuuj kopię main.py i schematy.py z tematu 56. Przywróć wymagane pole pobrania, bez default. Zapis w tej lekcji jest w pamięci procesu: restart usuwa albumy i zaczyna ID od 1. Utrzymuj oddzielny rosnący licznik ID; nie wyliczaj nowego ID z długości listy.

| Metoda i adres | Sukces | Brak zasobu |
| --- | --- | --- |
| GET /albumy | 200, lista (również pusta) | Nie dotyczy |
| GET /albumy/{id} | 200, album | 404 |
| POST /albumy | 201, album z nadanym id | Nie dotyczy |
| PUT /albumy/{id} | 200, cały zaktualizowany album | 404 |
| DELETE /albumy/{id} | 204, bez ciała | 404 |

Pola wejścia: tytul i pobrania. Schemat waliduje je przed zmianą stanu; id nadaje serwer. Nie zaimplementowano PATCH. Uruchom `py -m uvicorn main:app --reload`. Dla tego ćwiczenia nie zmieniaj kodu między kolejnymi operacjami testowej sekwencji, bo przeładowanie resetuje pamięć.

## Zadanie 1. Dodawanie i lista

- Połącz schemat z tematu 56 z kodem GET i POST z tej lekcji.
- Od pustego stanu dodaj Poranek=120 i Wieczór=80. Pobierz listę.

**Wynik kontrolny:** 201 dla obu zapisów, lista dwóch różnych ID.

## Zadanie 2. Edycja po ID

- Dodaj PUT. Zmień pobrania pierwszego albumu na 121, zachowując tytuł.
- Spróbuj zmienić nieistniejący album 999.
- Porównaj pełną listę przed i po nieudanej zmianie.

**Wynik kontrolny:** pierwszy album zmieniony, 999 daje 404 bez dodatkowego rekordu.

## Zadanie 3. Usunięcie i kolejny zapis

- Usuń pierwszy album. Ponownie wyślij DELETE dla tego samego ID.
- Dodaj trzeci album Noc z pobrania=0.
- Sprawdź, czy Wieczór zachował ID, a nowy album nie przejął usuniętego ID.

**Wynik kontrolny:** 204, potem 404; nowe id=3, Wieczór nadal id=2.

## Zadanie 4. Błędne dane nie zmieniają stanu

- Wyślij PUT dla Wieczoru z pobrania=-1, potem bez pola pobrania.
- Używaj modelu z wymaganymi polami, bez wartości domyślnej z ćwiczenia 56.3.
- Pobierz Wieczór ponownie i sprawdź zachowanie poprzednich danych.

**Wynik kontrolny:** dwa statusy 422, zapisane wartości bez zmian.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
