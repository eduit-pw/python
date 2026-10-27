# Temat 21. Wyjaśnienia do praktyki

## Wyjątek i zakres try

Wyjątek przerywa zwykły przebieg i szuka pasującego except. Obejmuj try operacje, których spodziewany błąd obsługujesz. Zbyt szeroki blok może ukryć błąd programistyczny.

## Rodzaje błędów

int niepoprawnego tekstu zgłasza ValueError, dzielenie przez 0 ZeroDivisionError, brak klucza KeyError. Zapis, który nie jest zgodny ze składnią, wymaga poprawy kodu.

## Kolejność except

Umieszczaj szczegółowe typy przed ogólnymi. Pierwszy pasujący except obsłuży wyjątek. Nie używaj samego except do zwykłej walidacji danych.

## else i finally

else przy try działa, gdy blok try zakończył się bez wyjątku. finally wykonuje sprzątanie przy zwykłym zakończeniu i obsłudze wyjątku. Nie zastępuje wyniku operacji.

## Ponawianie wejścia

Błąd konwersji obsłuż w except, a poprawny typ ze złym zakresem osobnym if. Po sukcesie zwróć wartość lub zakończ pętlę. Po błędzie nie używaj nieprzypisanej zmiennej.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
