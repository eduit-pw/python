# Ćwiczenia: Jak działa sieć i strony internetowe: zapytania i odpowiedzi, przesyłanie danych oraz zasady API

**Temat 50 | Lekcje 103-104**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Lokalny serwer i dane

Dołączony `http_lab/dane.json` zawiera dwa albumy z polami tytul i pobrania (120 i 80). W pierwszym terminalu, z folderu lekcji, uruchom:

```powershell
py -m http.server 8000 --bind 127.0.0.1 --directory http_lab
```

Otwórz `http://127.0.0.1:8000/dane.json`. Klienta `klient.py` uruchamiaj z drugiego terminalu. Użyj urllib.request.urlopen z limitem czasu, odkoduj UTF-8 i przetwórz json.loads. Sprawdzaj obecność tytułu typu str oraz pobrania dokładnie int >=0; bool nie jest poprawną liczbą pobrań. Próby z błędnym JSON wykonuj na kopii, a potem przywróć dane.

## Zadanie 1. Sprawdź odpowiedź w przeglądarce

- Użyj pliku http_lab/dane.json i uruchom serwer według powyższej instrukcji.
- W narzędziach przeglądarki otwórz kartę Network i pobierz /dane.json.
- Zapisz metodę, status, Content-Type i liczbę albumów.

**Wynik kontrolny:** GET, 200, application/json, 2 albumy.

## Zadanie 2. Raport klienta

- Pobierz dane.json przez urlopen i odczytaj listę słowników.
- Wypisz tytuły oraz sumę pola pobrania.
- Sprawdź, czy otrzymany obiekt jest listą, a pobrania są nieujemnymi int.

**Wynik kontrolny:** Poranek, Wieczór, suma 200.

## Zadanie 3. Rozróżnij błędy

- Przechwyć HTTPError przed URLError. Dodaj osobną obsługę JSONDecodeError.
- Pobierz /brak.json, zatrzymaj serwer i pobierz ponownie, a potem podaj błędny JSON.
- Dla błędnego JSON użyj pliku dane.json z samym znakiem „{”.

 import błędów z urllib.error i json.

**Wynik kontrolny:** 404, błąd połączenia oraz błąd formatu.

## Zadanie 4. Umowa przyszłego API

- Opisz trzy operacje: GET /albumy/, POST /albumy/ i DELETE /albumy/7/.
- Dla dodawania podaj przykład JSON z tytułem i liczbą pobrań.
- Ustal odpowiedzi: odczyt 200, dodanie 201, usunięcie bez treści 204.

**Wynik kontrolny:** opis metody, adresu, wejścia i wyjścia dla każdej operacji.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
