# Temat 65. Wyjaśnienia do praktyki

## Logger i poziom

Logger emituje zdarzenia DEBUG, INFO, WARNING, ERROR i CRITICAL. Ustawiony próg przepuszcza poziom równy lub wyższy. INFO nie zapisze DEBUG.

## Handler i format

Handler wskazuje miejsce zapisu, formatter postać wiersza. Podaj czas, poziom i komunikat. Konfigurację wykonaj raz, zanim rozpoczniesz przetwarzanie.

## Tryb pliku

Tryb dopisywania zachowuje historię między uruchomieniami. UTF-8 chroni polskie znaki. Przed testem liczby wpisów zacznij od jawnie ustalonego stanu pliku.

## Wyjątek w logu

logger.exception wewnątrz except zapisuje traceback na poziomie ERROR. warning może opisać odrzucony rekord bez traceback. Nie loguj jednego błędu kilka razy w różnych warstwach.

## Duplikaty

Dwa handlery mogą zapisać to samo zdarzenie dwa razy. Powielanie addHandler przy każdym wywołaniu pogarsza problem. Skontroluj konfigurację i propagację loggera.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
