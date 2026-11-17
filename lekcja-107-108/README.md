# Ćwiczenia: Podstawy HTTP i pierwsza aplikacja Django: projekt, ustawienia i adresy podstron

**Temat 54 | Lekcje 107-108**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Każde zadanie ma osobny starter. Zadania rozwijające aplikację wykonuj na kopii poprzedniego etapu, zgodnie z instrukcją startera.

## Utworzenie projektu

Utwórz lokalne środowisko i zainstaluj Django 5.2 według instrukcji na stronie głównej. Z folderu lekcji wykonaj:

```powershell
mkdir szkola_web
cd szkola_web
py -m django startproject szkola .
py manage.py startapp strony
py manage.py migrate
py manage.py runserver
```

Wybierz interpreter swojego venv; polecenie py musi używać tego samego środowiska. Jeśli używasz jawnej ścieżki do interpretera, zastąp py tą ścieżką. Po `startapp` dodaj `strony` do INSTALLED_APPS. Widoki używają HttpResponse; funkcja lekcja(request, numer) zwraca `Lekcja N`, gdzie N to przekazany numer. Kolejne lekcje kontynuują projekt, więc zachowaj działający katalog szkola_web.

## Sposób pracy podczas bloku

| Etap | Czas | Co robisz |
| --- | ---: | --- |
| Podstawy HTTP | 0–10 min | Odczytujesz metodę, URL, status i nagłówki w przeglądarce. |
| Django i demonstracja | 10–25 min | Rozpoznajesz projekt, aplikację, widok i adres. |
| Zadanie 1 | 25–40 min | Uruchamiasz projekt z prowadzącym. |
| Zadanie 2 | 40–60 min | Łączysz adres ze stroną główną i sprawdzasz 404. |
| Zadanie 3 | 60–78 min | Dodajesz drugi widok i obserwujesz żądanie. |
| Sprawdzenie i Git | 78–85 min | Uruchamiasz oba adresy i zapisujesz zmianę. |
| Zakończenie | 85–90 min | Zachowujesz projekt do następnej lekcji. |

Zadanie 4 i diagnoza są dla chętnych lub do samodzielnej kontynuacji.

**Podczas pracy:** korzystaj z [tabel składni i krótkich wzorców](KONSTRUKCJE.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Uruchom projekt

**Punkt wyjścia:** [starter zadania 1](startery/zadanie1/README.md).

- Utwórz szkola_web, venv, projekt szkola i aplikację strony według poleceń powyżej.
- Uruchom migrate, a potem runserver. Otwórz http://127.0.0.1:8000/.
- Zapisz wersję Pythona i Django. Zatrzymaj serwer przez Ctrl+C.

**Wynik kontrolny:** domyślna strona Django przed dodaniem własnych adresów.

## Zadanie 2. Strona główna

**Punkt wyjścia:** [starter zadania 2](startery/zadanie2/README.md).

- Dodaj aplikację do INSTALLED_APPS. Utwórz widok start i dwa pliki konfiguracji URL.
- Użyj include do dołączenia adresów aplikacji w pustym prefiksie.
- Uruchom serwer i sprawdź / oraz nieistniejącą /brak/.

**Wynik kontrolny:** „Witaj w szkole!” i status 200. Dla /brak/: 404.

## Zadanie 3. Kontakt

**Punkt wyjścia:** [starter zadania 3](startery/zadanie3/README.md).

- Dodaj widok kontakt z odpowiedzią „Kontakt: sekretariat”.
- W strony/urls.py dodaj path dla kontakt/ i nazwę „kontakt”.
- Sprawdź /kontakt/ oraz ponownie /. W narzędziach przeglądarki otwórz Network. Odczytaj metodę GET, ścieżkę, status i Content-Type. Porównaj odpowiedź z wejściem na /brak/.

**Wynik kontrolny:** obie podstrony działają i zwracają własny tekst.

## Zadanie 4. Dla chętnych: Numer lekcji

**Punkt wyjścia:** [starter zadania 4](startery/zadanie4/README.md).

- Dodaj widok lekcja i ścieżkę lekcja/<int:numer>/.
- Sprawdź /lekcja/51/, /lekcja/0/, /lekcja/abc/ i /lekcja/-1/.
- Wyjaśnij różnicę między tekstem w URL a typem parametru widoku.

**Wynik kontrolny:** Lekcja 51, Lekcja 0 oraz dwa statusy 404.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)

## Utrwalanie Git w ramach tego bloku

Przed zmianą sprawdź `git status`, a po działającej poprawce obejrzyj `git diff`. Zapisz mały commit z opisem wykonanej zmiany. Czynność zajmuje 2–3 minuty przewidziane na sprawdzenie pracy.

## HTTP i Django

Dla `http://127.0.0.1:8000/kontakt/` host to `127.0.0.1`, port to `8000`, a ścieżka to `/kontakt/`. Przeglądarka wysyła żądanie, a widok Django tworzy odpowiedź. Działająca strona zwraca 200. Dla nieznanego adresu serwer może zwrócić 404. Brak połączenia to osobny problem. POST przesyła dane do przetworzenia. Użyjesz go przy formularzach w temacie 57.
