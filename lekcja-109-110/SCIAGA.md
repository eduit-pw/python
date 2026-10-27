# Temat 53. Wyjaśnienia do praktyki

## Model ORM

Klasa dziedzicząca po models.Model opisuje tabelę. Atrybuty pól określają typy i ograniczenia. Instancja modelu odpowiada rekordowi, a pk jego kluczowi.

## Migracje

makemigrations tworzy opis zmiany schematu, migrate stosuje go w bazie. Modyfikacja pliku modelu sama nie zmienia tabeli. Pliki migracji należą do repozytorium.

## Zapytania

objects.all i filter tworzą QuerySet, order_by określa porządek. first zwraca obiekt albo None. get dla braku lub wielu wyników zgłasza wyjątek.

## Zapis i walidacja

save zapisuje stan instancji, ale nie wywołuje automatycznie pełnego full_clean. Walidację modelu, formularza i ograniczenia bazy rozróżniaj. Nie zakładaj, że nazwa typu pola rozwiązuje wszystkie błędy wejścia.

## Domyślna wartość

Nowe pole z default pozwala określić wartość dla rekordów. Po migracji sprawdź zachowanie istniejących danych. Zmieniaj tylko wskazany obiekt, nie wszystkie rekordy.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
