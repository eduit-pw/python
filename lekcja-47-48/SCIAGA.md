# Temat 24. Wyjaśnienia do praktyki

## setUp

setUp wykonuje się przed każdą metodą testową. Przygotuj w nim nowy obiekt i niezależne dane. Zmiana w jednym teście nie powinna przygotowywać stanu następnego.

## tearDown

tearDown działa po metodzie testowej, również po nieudanej asercji, gdy setUp zakończył się poprawnie. Zamknij otwarte zasoby. Nie jest potrzebny dla każdego zwykłego obiektu.

## StringIO

io.StringIO jest buforem tekstowym w pamięci. write dopisuje tekst, getvalue zwraca całość, close zamyka bufor. Zawartość odczytaj przed zamknięciem.

## Przypadki brzegowe

Sprawdź dolny i górny próg, wartości obok progu, puste wejście i błędny typ zgodnie z kontraktem. Każdy przypadek ma mieć określone oczekiwanie.

## Stan współdzielony

Nowa instancja TestCase nie resetuje automatycznie liczników klas aplikacji. Przygotuj i przywróć taki stan świadomie. Osobna baza lub folder tymczasowy chroni dane innych testów.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
