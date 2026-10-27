# Temat 56. Wyjaśnienia do praktyki

## Model Pydantic

BaseModel opisuje oczekiwane pola i typy. Obiekt modelu zawiera zwalidowane dane. Field dodaje ograniczenia, np. ge=0 lub max_length=80.

## Konwersja i strict

Domyślnie część typów może być przekształcana. strict=True pozwala wymagać ścisłego rodzaju danych dla pola. Bool i tekst liczbowy odrzuć, gdy kontrakt wymaga liczby całkowitej.

## Walidator tekstu

field_validator pozwala oczyścić tytuł i sprawdzić jego sens. Po strip same spacje stają się pustym napisem. Kolejność walidacji długości i oczyszczania musi odpowiadać kontraktowi.

## Pola dodatkowe i brakujące

ConfigDict(extra="forbid") odrzuca nieznane pola. Pole bez wartości domyślnej jest wymagane. default=0 pozwala je pominąć, więc świadomie zmienia umowę.

## Schemat odpowiedzi

response_model opisuje dane zwracane klientowi. ID może nadawać serwer, chociaż model wejścia go nie przyjmuje. W /docs sprawdź osobno schemat wejścia i wyniku.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
