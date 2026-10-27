# Temat 55. Wyjaśnienia do praktyki

## FastAPI i app

app = FastAPI() tworzy aplikację. Dekorator @app.get wiąże funkcję z metodą i ścieżką. Słownik wyniku jest serializowany do odpowiedzi JSON.

## Parametr ścieżki

Nazwa w /kwadrat/{liczba} pasuje do parametru funkcji. Adnotacja int uruchamia konwersję i walidację. Niepoprawny zapis daje odpowiedź 422.

## Query i wartość domyślna

Parametr funkcji nieujęty w ścieżce może pochodzić z query. Wartość domyślna pozwala go pominąć. Adres /powitanie?imie=Anna przekazuje napis do argumentu imie.

## Uvicorn

python -m uvicorn main:app uruchamia obiekt app z modułu main. --reload przeładowuje przy zmianie kodu i służy pracy developerskiej. Zatrzymaj poprzedni serwer przed zajęciem tego samego portu.

## Dokumentacja i status

/docs pokazuje operacje i pozwala je wywołać. Nieistniejąca ścieżka daje 404, niedozwolona metoda 405, błąd danych 422. To różne przyczyny, a nie jeden ogólny problem połączenia.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
