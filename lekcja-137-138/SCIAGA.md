# Temat 66. Wyjaśnienia do praktyki

## ArgumentParser

ArgumentParser opisuje argumenty i generuje pomoc. add_argument definiuje nazwę, typ oraz domyślną wartość. parse_args odczytuje rzeczywiste argumenty procesu.

## Argument i opcja

plik może być wymaganym argumentem pozycyjnym, --min opcją z wartością, --verbose przełącznikiem store_true. Pokaż te różnice w --help.

## Kody zakończenia

0 oznacza sukces, 2 błąd użycia argparse, a umówiony 1 błąd danych lub pliku. stdout przeznacz na wynik, stderr na diagnostykę. Sprawdzaj kod procesu po błędzie.

## Konfiguracja .env

load_dotenv z override=False nie zastępuje istniejących zmiennych środowiska. Argument CLI może mieć najwyższy priorytet, potem środowisko, plik .env i wartość domyślna.

## Walidacja przed raportem

Sprawdź argumenty i dane, zanim utworzysz plik wyjścia. Brak pliku lub błędny JSON nie powinien zostawić raportu udającego sukces. Sekretów nie dołączaj do .env.example.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
