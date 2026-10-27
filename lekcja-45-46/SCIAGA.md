# Temat 23. Wyjaśnienia do praktyki

## TestCase i metoda testowa

Klasa dziedziczy po unittest.TestCase. Metoda o nazwie zaczynającej się od test_ opisuje przypadek. Test przygotowuje dane, wykonuje operację i sprawdza wynik.

## Asercje

assertEqual porównuje wartości, assertTrue i assertFalse sprawdzają prawdziwość, assertIs tożsamość. Wartość oczekiwaną wyznacz niezależnie od badanego kodu.

## Oczekiwany wyjątek

with self.assertRaises(TypBledu) sprawdza zgłoszenie określonego wyjątku. Jeśli błąd nie nastąpi, test nie przejdzie. Przy odrzuconej zmianie sprawdź także niezmieniony stan.

## FAIL i ERROR

FAIL oznacza niespełnioną asercję. ERROR oznacza nieobsłużony błąd wykonania testu. Czytaj nazwę testu i traceback, nie tylko ostatnie słowo podsumowania.

## Import i uruchomienie

Import modułu testowanego nie powinien pytać o input. Interakcję umieść pod if __name__ == "__main__". Uruchom python -m unittest discover -v w folderze konkretnego projektu.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
