# Ćwiczenia: Komunikacja sieciowa i integracja z zewnętrznymi serwisami oraz modelami AI za pomocą biblioteki requests

**Temat 63 | Lekcje 131-132**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Serwer do ćwiczeń

Dołączony `serwer.py` jest lokalnym źródłem danych do testowania klienta. Uruchom go w pierwszym terminalu przez `py serwer.py`; własny `klient.py` uruchamiaj z drugiego terminalu. Adres bazowy to http://127.0.0.1:8000. Zainstaluj requests. Serwer korzysta wyłącznie z biblioteki standardowej. GET /albumy zwraca dwa rekordy: Poranek=120 i Wieczór=80. GET /nie-json zwraca zwykły tekst, /brak daje 404, /wolno odpowiada z opóźnieniem. Używaj timeout, raise_for_status i kontroli JSON oraz pól.

Dla POST /ai-demo wyślij JSON z polem tekst oraz nagłówek Authorization: Bearer demo_token. Token demonstracyjny odczytaj w kliencie ze zmiennej API_TOKEN. W PowerShell przed próbą ustaw `$env:API_TOKEN = "demo_token"`. To lokalna symulacja, niewymagająca konta ani płatnego dostawcy AI.

## Zadanie 1. Raport z lokalnego API

- Uruchom dołączony serwer.py według instrukcji powyżej. Pobierz /albumy przez requests.
- Sprawdź status i pola, wypisz tytuły oraz sumę pobrań.

**Wynik kontrolny:** Poranek, Wieczór, suma 200.

## Zadanie 2. Filtr query

- Pobierz listę z params={"min":100}, a potem z min=200.
- Nie dopisuj wartości query ręcznie do adresu. Obsłuż pustą listę.

**Wynik kontrolny:** Poranek dla 100, pusta lista dla 200.

## Zadanie 3. Próby błędne

- Wyślij GET /brak, GET /nie-json i GET /wolno z timeout=0.1.
- Zatrzymaj serwer i ponownie wyślij GET /albumy.
- Dla każdej próby wyświetl komunikat odpowiadający przyczynie.

**Wynik kontrolny:** błąd HTTP, JSON, timeout oraz połączenia.

## Zadanie 4. Integracja demonstracyjna AI

- Wyślij tekst do /ai-demo z tokenem demo_token z API_TOKEN.
- Sprawdź status i pole odpowiedz. Powtórz bez tokenu i z tokenem błędnym.
- Nie wypisuj tokenu. Opisz, które elementy zmienisz dla rzeczywistego dostawcy.

**Wynik kontrolny:** 200 i odpowiedź demo albo 401 dla braku poprawnego tokenu.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
