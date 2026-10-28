# Ćwiczenia: Nowoczesne usługi sieciowe w FastAPI: uruchomienie serwera i pierwsze punkty dostępu

**Temat 55 | Lekcje 113-114**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Uruchomienie usługi

Utwórz `main.py` i obiekt `app = FastAPI()`. Samodzielnie dodaj GET /status zwracający słownik `{"stan": "ok"}`. Używaj pliku requirements.txt i środowiska FastAPI z instrukcji głównej. Po zapisaniu kodu uruchom:

```powershell
py -m uvicorn main:app --reload
```

Adres bazowy: `http://127.0.0.1:8000`. Dokumentacja: `/docs`. W /kwadrat/{liczba} odpowiedź ma pola `liczba` i `kwadrat`. Zatrzymaj inne serwery używające portu 8000.

## Sposób pracy podczas bloku

| Etap | Czas | Co robisz |
| --- | ---: | --- |
| Wyjaśnienia i demonstracja | 0-25 min | Czytasz przykład, przewidujesz wynik i zadajesz pytania. |
| Zadanie 1 z prowadzącym | 25-35 min | Uruchamiasz pierwszy wariant i objaśniasz kluczowy zapis. |
| Zadanie 2 wspólnie | 35-50 min | Proponujesz kolejne kroki, sam zapisujesz kod. |
| Zadanie 3 samodzielnie | 50-70 min | Realizujesz kontrakt i wykonujesz próby. |
| Zadanie 4 lub diagnoza błędu | 70-85 min | Sprawdzasz przypadki graniczne i poprawiasz program. |
| Zakończenie | 85-90 min | Zapisujesz kod, jeden wniosek i wykonane próby. |

Tempo ustala nauczyciel. Jeśli zadanie 4 jest większe, stanowi kontynuację na kolejnych zajęciach lub zastępuje dodatkową diagnozę. Zadania dodatkowe nie są warunkiem ukończenia podstawowego bloku.

**Podczas pracy:** korzystaj z [tabel składni i krótkich wzorców](SCIAGA.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Usługa działa

- Utwórz main.py z GET /status według powyższej umowy i uruchom Uvicorn.
- Sprawdź /status w przeglądarce oraz przez Try it out w /docs.

**Wynik kontrolny:** 200 oraz {"stan":"ok"}.

## Zadanie 2. Parametr liczbowy

- Dodaj /kwadrat/{liczba} z parametrem int. Zwróć liczbę i jej kwadrat.
- Wyślij wartości 5, -3 i abc. Nie przechwytuj błędu typu ręcznie.

**Wynik kontrolny:** 25, 9 oraz odpowiedź 422 dla abc.

## Zadanie 3. Opcjonalne query

- Dodaj /powitanie z parametrem imie: str = "Uczeń".
- Zwróć {"tekst": "Cześć, ..."}. Sprawdź brak parametru i imie=Anna.

**Wynik kontrolny:** Cześć, Uczeń oraz Cześć, Anna.

## Zadanie 4. Różne błędy HTTP

- Wyślij GET /brak, POST /status i GET /kwadrat/abc.
- Zapisz metodę, URL, status i krótki opis przyczyny każdego wyniku.

**Wynik kontrolny:** kolejno 404, 405 i 422.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
