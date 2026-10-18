# Ćwiczenia: Tworzenie programów uruchamianych z wiersza poleceń z opcjami i parametrami (argparse, dotenv)

**Temat 66 | Lekcje 137-138**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Kontrakt programu CLI

Napisz własny raport.py z argparse. Argument pozycyjny plik jest wymagany; --min ma typ int i domyślnie 0; --wyjscie jest opcjonalną ścieżką; --verbose jest przełącznikiem. Dane są listą albumów: tytul typu str i pobrania dokładnie int >=0. Dołączony dane.json zawiera Poranek=120 oraz Wieczór=80. Wybierz albumy z pobrania >= próg i wypisz po jednym tytule w wierszu albo `Brak albumów`. --wyjscie przenosi raport do pliku UTF-8 z końcowym znakiem nowego wiersza; bez tej opcji użyj stdout. --verbose wypisuje liczbę wybranych na stderr.

Błąd argumentów: kod 2; błąd pliku, JSON lub danych: komunikat na stderr i kod 1; sukces: 0. Nie twórz raportu po błędzie odczytu. Dla --min <0 użyj parser.error. Po wykonaniu programu kod sprawdzisz w PowerShell jako `$LASTEXITCODE`.

```powershell
py raport.py dane.json --min 100 --wyjscie raport.txt
py raport.py --help
```

W osobnym config_demo.py wczytaj .env obok skryptu przez load_dotenv(..., override=False). Reguła wyboru URL: niepuste --url, następnie API_URL już w środowisku lub wczytane z .env, na końcu http://127.0.0.1:8000. Plik .env.example jest wzorem; skopiuj go lokalnie do .env do próby. W tym ćwiczeniu adres nie jest sekretem.

## Zadanie 1. Raport z progiem

- Napisz i uruchom raport.py dla danych Poranek=120 i Wieczór=80, z --min 100.
- Zapisz raport do raport.txt przez --wyjscie. Użyj UTF-8.
- Powtórz dla progu 200.

**Wynik kontrolny:** Poranek dla 100, komunikat Brak albumów dla 200.

## Zadanie 2. Pomoc i błędne argumenty

- Sprawdź --help, brak argumentu pliku, --min abc i --min -1.
- Porównaj komunikaty i kod zakończenia.

**Wynik kontrolny:** pomoc z kodem 0, błędne użycie z kodem 2.

## Zadanie 3. Błąd danych wejściowych

- Uruchom raport.py dla nieistniejącego pliku oraz pliku z samym znakiem {.
- Sprawdź komunikat i brak pliku raportu po nieudanym odczycie.
- Popraw plik i ponów próbę.

**Wynik kontrolny:** kod 1 dla obu błędów, poprawny raport z kodem 0.

## Zadanie 4. Priorytet konfiguracji

- W osobnym config_demo.py dodaj --url, load_dotenv i os.getenv według reguły opisanej powyżej.
- Porównaj brak konfiguracji, API_URL w .env, API_URL w środowisku i --url.
- Używaj adresów demonstracyjnych. Nie wypisuj sekretów.

**Wynik kontrolny:** CLI wygrywa ze środowiskiem, środowisko z .env, potem działa domyślna wartość.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
