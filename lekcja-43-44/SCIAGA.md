# Temat 22. Wyjaśnienia do praktyki

## raise

raise ValueError(komunikat) zgłasza błąd z opisem. Funkcja walidująca zgłasza wyjątek lub zwraca poprawną wartość. O sposobie pokazania błędu decyduje kod wywołujący.

## Własny typ wyjątku

class OcenaError(ValueError) tworzy szczegółowy rodzaj błędu wartości. except ValueError przechwyci również ten podtyp. Jeśli go odróżniasz, except OcenaError umieść wcześniej.

## Typ a wartość

TypeError oznacza niewłaściwy typ argumentu, ValueError niedopuszczalną wartość odpowiedniego typu. Gdy kontrakt wymaga dokładnie int, pamiętaj, że bool jest podtypem int.

## Walidacja przed zapisem

Sprawdź argumenty przed zmianą listy, licznika lub pola obiektu. Odrzucona operacja ma pozostawić stan niezmieniony. Konstruktor nie powinien tworzyć częściowo zaakceptowanych danych.

## Dane w wyjątku

Obiekt wyjątku może zawierać odrzuconą wartość w atrybucie. super().__init__(komunikat) ustawia jego tekst. Nie zastępuj błędu poprawnym wynikiem 0, jeśli umowa tego nie przewiduje.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
