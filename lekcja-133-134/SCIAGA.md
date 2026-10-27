# Temat 64. Wyjaśnienia do praktyki

## HTML i parser

BeautifulSoup przekształca HTML w drzewo. Podaj parser html.parser. Wczytaj tekst w odpowiednim kodowaniu. Parser nie wykonuje JavaScript strony.

## Selektory CSS

select zwraca listę dopasowań, select_one pojedyncze dopasowanie lub None. article.album wybiera article z klasą album. Zmiana struktury strony może zmienić liczbę wyników.

## Tekst i atrybut

get_text(strip=True) pobiera tekst węzła. get("data-id") odczytuje atrybut. Najpierw sprawdź istnienie węzła, potem wołaj jego metody.

## Konwersja i reguła braku

Pobrania odczytane z HTML są tekstem do konwersji. Brak pola i błędna liczba są różnymi przypadkami. Wartość domyślną 0 stosuj wyłącznie tam, gdzie ustalono taką umowę.

## Eksport i kontrola importu

Zapisuj dane do CSV z nagłówkiem i UTF-8. Sprawdź liczbę rekordów oraz sumę kontrolną. Nagły spadek liczby kart może wskazywać zmianę źródła, a nie poprawny pusty wynik.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
