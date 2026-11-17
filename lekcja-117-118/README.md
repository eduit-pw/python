# Ćwiczenia: Nowoczesne usługi sieciowe w FastAPI: uruchomienie serwera i pierwsze punkty dostępu

**Temat 59 | Lekcje 117-118**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Każde zadanie ma osobny starter. Zadania rozwijające aplikację wykonuj na kopii poprzedniego etapu, zgodnie z instrukcją startera.

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
| Klient HTTP i JSON | 70–82 min | Wywołujesz działające /status z drugiego terminala. |
| Sprawdzenie i Git | 82–85 min | Wykonujesz ostatnią próbę i zapisujesz zmianę. |
| Zakończenie | 85-90 min | Zapisujesz kod, jeden wniosek i wykonane próby. |

Zadanie 4 i diagnoza są dla chętnych lub do samodzielnej kontynuacji. W podstawowym bloku wykonujesz trzy zadania i uruchamiasz dostarczonego klienta HTTP.

**Podczas pracy:** korzystaj z [tabel składni i krótkich wzorców](KONSTRUKCJE.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Usługa działa

**Punkt wyjścia:** [starter zadania 1](startery/zadanie1/README.md).

- Utwórz zadanie1.py z GET /status według powyższej umowy i uruchom Uvicorn.
- Sprawdź /status w przeglądarce oraz przez Try it out w /docs.

**Wynik kontrolny:** 200 oraz {"stan":"ok"}.

## Zadanie 2. Parametr liczbowy

**Punkt wyjścia:** [starter zadania 2](startery/zadanie2/README.md).

- Dodaj /kwadrat/{liczba} z parametrem int. Zwróć liczbę i jej kwadrat.
- Wyślij wartości 5, -3 i abc. Nie przechwytuj błędu typu ręcznie.

**Wynik kontrolny:** 25, 9 oraz odpowiedź 422 dla abc.

## Zadanie 3. Opcjonalne query

**Punkt wyjścia:** [starter zadania 3](startery/zadanie3/README.md).

- Dodaj /powitanie z parametrem imie: str = "Uczeń".
- Zwróć {"tekst": "Cześć, ..."}. Sprawdź brak parametru i imie=Anna.

**Wynik kontrolny:** Cześć, Uczeń oraz Cześć, Anna.

## Zadanie 4. Dla chętnych: Różne błędy HTTP

**Punkt wyjścia:** [starter zadania 4](startery/zadanie4/README.md).

- Wyślij GET /brak, POST /status i GET /kwadrat/abc.
- Zapisz metodę, URL, status i krótki opis przyczyny każdego wyniku.

**Wynik kontrolny:** kolejno 404, 405 i 422.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)

## Utrwalanie Git w ramach tego bloku

Przed zmianą sprawdź `git status`, a po działającej poprawce obejrzyj `git diff`. Zapisz mały commit z opisem wykonanej zmiany. Czynność zajmuje 2–3 minuty przewidziane na sprawdzenie pracy.


## Klient HTTP: odpowiedź JSON

W minutach 70–82, przy działającym serwerze, uruchom `klient_http.py` w drugim terminalu. Nauczyciel używa pliku z `kod/`, a uczeń kopii ze `startery/`. Polecenie: `python klient_http.py`. Wynik: `{'stan': 'ok'}`. W funkcji zmień domyślny URL na adres `/brak`: otrzymasz błąd HTTP 404. Po zatrzymaniu serwera wróć do `/status`: zobaczysz błąd połączenia. Nie wykonuj obu zmian naraz. Kod korzysta z biblioteki standardowej.

`read()` zwraca bajty, `decode("utf-8")` daje tekst, a `json.loads()` tworzy obiekt Pythona. Po odczycie sprawdzamy strukturę danych. Status sukcesu sam nie gwarantuje oczekiwanych pól. HTTPError obsługujemy przed URLError, bo jest jego podklasą. Odpowiedź bez treści, np. 204, nie nadaje się do bezwarunkowego odczytu JSON. Metody zapisu i pełne operacje CRUD rozwijamy w tematach 60–61.

Zadanie 4 i diagnoza są rozszerzeniem dla chętnych. Podstawowy blok obejmuje trzy zadania oraz krótkie uruchomienie dostarczonego klienta.
