# Temat 42. Wyjaśnienia do praktyki

## Sygnał i slot

Sygnał opisuje zdarzenie, slot jest funkcją reagującą na nie. connect otrzymuje funkcję bez nawiasów. Jeden sygnał może dostarczać argument, np. nową wartość.

## Stan licznika

self.licznik przechowuje wartość niezależnie od tekstu etykiety. Po zmianie stanu odśwież widok. Reset ustawia wartość, a nie tworzy nowego połączenia sygnału.

## textChanged

textChanged reaguje przy każdej zmianie tekstu, również programowej. Długość obejmuje spacje. Pusty napis daje 0.

## valueChanged

Suwak emituje zmianę wartości. W obsłudze odczytaj R, G i B, a następnie odśwież kolor i podpis. Ustal zakres 0-255 oraz początkowy stan wszystkich kontrolek.

## Podgląd i zatwierdzona próbka

Bieżący podgląd zmienia się na żywo. Zapisaną próbkę aktualizuje tylko przycisk. Przechowuj te dwa stany oddzielnie i sprawdź zmianę suwaka po zapisaniu próbki.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
