# Temat 51. Wyjaśnienia do praktyki

## Projekt i aplikacja

Projekt Django zawiera konfigurację serwisu, aplikacja wydzieloną funkcjonalność. startproject tworzy projekt, startapp aplikację. Dodaj aplikację do INSTALLED_APPS.

## URL i widok

path wiąże wzorzec adresu z funkcją widoku. include dołącza adresy aplikacji. Widok przyjmuje request i zwraca HttpResponse. Sam napis nie jest pełnym obiektem odpowiedzi.

## Parametr ścieżki

<int:numer> przechwytuje nieujemny zapis liczby z URL i przekazuje int. Niedopasowany adres daje 404. Nazwa parametru widoku musi pasować do wzorca.

## Polecenia manage.py

migrate przygotowuje tabele, runserver uruchamia serwer developerski. Polecenia wykonuj z katalogu manage.py tym samym interpreterem. Ctrl+C zatrzymuje serwer.

## Środowisko lokalne

Serwer developerski służy do ćwiczeń. Wersję Django i interpreter zapisz rzeczywiście zainstalowane. Zależności odtwarzaj z requirements, bez kopiowania .venv.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
