# Ćwiczenia: Praktyczny sprawdzian umiejętności: projektowanie i implementacja aplikacji okienkowej z interfejsem graficznym

**Temat 49 | Lekcje 101-102**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

### Polecenie i zakres pracy

- Wykonaj w PyQt6 aplikację szyfrującą małe litery a-z i spacje.
- Utwórz własny projekt z modułem cezar.py i plikiem main.py.
- Funkcję cezar(tekst, klucz) wykonaj samodzielnie lub odtwórz z wcześniejszej lekcji.
- Masz 90 minut. Przygotuj GUI, zapis, testy funkcji i krótką dokumentację. Adaptacja INF.04-02-25.06-SG, części I-III. Skrócony zakres lekcyjny, bez osobnej aplikacji konsolowej.

### Wymagane kontrolki

| Element | Wymaganie |
| --- | --- |
| Tytuł okna | Szyfrowanie. Wykonane przez + identyfikator ucznia |
| Klucz | QLineEdit, podpis „Podaj wartość klucza” |
| Wejście | QTextEdit, podpis „Podaj tekst” |
| Wynik | Pole tylko do odczytu, podpis „Tekst zaszyfrowany” |
| Przyciski | „Zaszyfruj” oraz „Zapisz szyfr w pliku” |

### Przykładowy wynik dla abc i klucza 3

- Wynik to def.
- Tekst wejściowy pozostaje.
- Wynik można zapisać. Widok własnej implementacji. Wykonaj układ z czytelnymi odstępami, mieszczący wszystkie kontrolki.

### Wygląd okna

| Element | Kolor lub format |
| --- | --- |
| Tło okna | CadetBlue, #5F9EA0 |
| Etykiety pól | AntiqueWhite, #FAEBD7 |
| Tekst wyniku | AliceBlue, #F0F8FF |
| Ramka wyniku | Ciągła, AntiqueWhite, zaokrąglone rogi |
| Przyciski | LightBlue, #ADD8E6 |

Wielkości i układ dostosuj do PyQt6 bez utraty czytelności.

### Działanie po „Zaszyfruj”

- Pobierz tekst i klucz z kontrolek. Spróbuj zamienić klucz na int.
- Jeżeli zamiana klucza się nie uda, zastosuj 0, zgodnie z arkuszem.
- Wywołaj cezar i pokaż wynik. Zachowaj spacje.
- Zakładamy poprawny tekst wejściowy: małe litery a-z i spacje. Nie dodawaj innego działania dla błędnego klucza. Pusty wynik ma być pustym napisem.

### Działanie po „Zapisz szyfr w pliku”

- Otwórz systemowy dialog zapisu i pobierz wskazaną ścieżkę.
- Anulowanie pozostawia dotychczasowy stan i nie tworzy pliku.
- Zapisz aktualnie wyświetlany wynik w UTF-8, bez dodatkowego nagłówka.
- Obsłuż OSError komunikatem, zachowując tekst w oknie. Obsługa anulowania i błędu zapisu są doprecyzowaniem adaptacji lekcyjnej.

### Testy funkcji szyfrującej

| Tekst | Klucz | Wynik |
| --- | ---: | --- |
| abc | 3 | def |
| xyz | 3 | abc |
| def | -3 | abc |
| abc | 29 | def |
| ab cd | 2 | cd ef |

Każdy przypadek sprawdź osobną metodą unittest z asercją i nazwą opisującą cel.

### Scenariusze testowania GUI

| Dane lub czynność | Oczekiwany rezultat |
| --- | --- |
| abc, klucz 0 | abc |
| abc, klucz x lub pusty | abc, bo przyjęto klucz 0 |
| Pusty tekst, klucz 3 | Pusty wynik |
| Zapis wyniku def | Plik zawiera dokładnie def |
| Anulowanie dialogu | Brak nowego pliku, wynik bez zmian |

### Oddawane pliki i dokumentacja

- Przekaż źródła, ewentualne .ui, testy oraz archiwum całego projektu bez venv.
- Dodaj zrzuty: działanie z dodatnim i ujemnym kluczem, błędny klucz oraz wyniki testów.
- Na zrzutach pokaż całe okno programu i narzędzie, w którym go uruchamiasz.
- W URUCHOMIENIE.md zapisz wersje narzędzi, polecenie uruchomienia i wykonane scenariusze. Nazwy plików i sposób oddania dotyczą tej adaptacji. Pełny arkusz ma własną strukturę folderów.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
