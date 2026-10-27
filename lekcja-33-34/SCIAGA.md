# Temat 17. Wyjaśnienia do praktyki

## Hermetyzacja

Obiekt udostępnia kontrolowane operacje zamiast dowolnego zmieniania stanu przez kod zewnętrzny. W Pythonie _nazwa jest konwencją. __nazwa uruchamia zmianę nazwy związaną z klasą, a nie pełne zabezpieczenie danych.

## @property

Getter property pozwala czytać obj.cena bez nawiasów i wykonywać przy tym metodę. Powinien zwrócić pole pomocnicze, np. self._cena.

## Setter

@cena.setter obsługuje przypisanie obj.cena = wartosc. Wykonaj sprawdzenia przed zmianą pola. Reakcję na zły zakres określa zadanie: może to być ignorowanie albo wyjątek.

## Inicjalizacja przez setter

Jeśli konstruktor użyje self.cena = cena, zadziała ta sama reguła walidacji. W zadaniu z ignorowaniem błędu ustaw najpierw bezpieczną wartość początkową.

## Rekursja i tylko odczyt

self.cena wewnątrz gettera cena wywoła go ponownie. W setterze to samo zrobi przypisanie do self.cena. Korzystaj z _cena. Property bez settera blokuje przypisanie przez tę właściwość.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
