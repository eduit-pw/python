# Ćwiczenia: Przeglądanie i sprawdzanie działania usługi za pomocą automatycznej strony Swagger UI i narzędzia typu Postman

**Temat 58 | Lekcje 119-120**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Projekt wejściowy

Pracuj na kopii własnego CRUD z tematu 57. Zachowaj GET /status, /docs i /openapi.json oraz model z dwoma wymaganymi polami. Użyj klienta Swagger UI lub Postmana. Przed pełnym cyklem kontrolnym zrestartuj usługę do pustego stanu, następnie nie zmieniaj kodu do zakończenia sekwencji. W /docs, po rozpakowaniu odpowiedniej operacji, zapisuj metodę, URL, JSON, status i ciało odpowiedzi. Żądania kieruj na http://127.0.0.1:8000.

## Zadanie 1. Odczyt opisu API

- Uruchom API z tematu 57 i porównaj /docs z /openapi.json.
- Znajdź schemat AlbumWejscie oraz kod sukcesu POST.
- Zapisz wymagane pola i dozwolony zakres pobrania.

**Wynik kontrolny:** tytul i pobrania wymagane, pobrania>=0, sukces 201.

## Zadanie 2. Cykl CRUD w kliencie API

- Od pustego stanu wykonaj POST, GET po otrzymanym ID, PUT i DELETE.
- Po zmianie odczytaj album, a po usunięciu spróbuj odczytać go jeszcze raz.
- Zapisz każde żądanie w kolekcji lub tabeli scenariuszy.

**Wynik kontrolny:** 201, 200, 200, 204, a na końcu 404.

## Zadanie 3. Próby negatywne

- Sprawdź POST bez tytułu, z pobrania=-1 i z dodatkowym id.
- Sprawdź nieistniejący ID oraz nieobsługiwaną metodę PATCH /albumy/1.
- Po nieudanych zapisach porównaj listę z jej poprzednim stanem.

**Wynik kontrolny:** 422 dla danych, 404 dla brakującego ID, 405 dla PATCH.

## Zadanie 4. Raport błędu

- Zmień lokalnie status sukcesu POST z 201 na 200 i uruchom scenariusz ponownie.
- Opisz URL, dane, oczekiwany i rzeczywisty wynik oraz kroki odtworzenia.
- Przywróć 201 i sprawdź przypadek jeszcze raz.

**Wynik kontrolny:** raport wskazuje naruszenie umowy statusu, po poprawce próba przechodzi.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
