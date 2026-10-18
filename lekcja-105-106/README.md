# Ćwiczenia: Pierwsze kroki z frameworkiem Django: tworzenie projektu, ustawienia i adresy podstron

**Temat 51 | Lekcje 105-106**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

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

## Zadanie 1. Uruchom projekt

- Utwórz szkola_web, venv, projekt szkola i aplikację strony według poleceń powyżej.
- Uruchom migrate, a potem runserver. Otwórz http://127.0.0.1:8000/.
- Zapisz wersję Pythona i Django. Zatrzymaj serwer przez Ctrl+C.

**Wynik kontrolny:** domyślna strona Django przed dodaniem własnych adresów.

## Zadanie 2. Strona główna

- Dodaj aplikację do INSTALLED_APPS. Utwórz widok start i dwa pliki konfiguracji URL.
- Użyj include do dołączenia adresów aplikacji w pustym prefiksie.
- Uruchom serwer i sprawdź / oraz nieistniejącą /brak/.

**Wynik kontrolny:** „Witaj w szkole!” i status 200. Dla /brak/: 404.

## Zadanie 3. Kontakt

- Dodaj widok kontakt z odpowiedzią „Kontakt: sekretariat”.
- W strony/urls.py dodaj path dla kontakt/ i nazwę „kontakt”.
- Sprawdź /kontakt/ oraz ponownie /.

**Wynik kontrolny:** obie podstrony działają i zwracają własny tekst.

## Zadanie 4. Numer lekcji

- Dodaj widok lekcja i ścieżkę lekcja/<int:numer>/.
- Sprawdź /lekcja/51/, /lekcja/0/, /lekcja/abc/ i /lekcja/-1/.
- Wyjaśnij różnicę między tekstem w URL a typem parametru widoku.

**Wynik kontrolny:** Lekcja 51, Lekcja 0 oraz dwa statusy 404.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
