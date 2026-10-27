# Temat 37. Wyjaśnienia do praktyki

## Warunek bazowy

Funkcja rekurencyjna wywołuje samą siebie dla mniejszego problemu. Warunek bazowy zatrzymuje wywołania. Brak postępu albo warunku końca prowadzi do RecursionError.

## Stos wywołań

Każde wywołanie ma własne parametry i zmienne lokalne. Powroty następują w odwrotnej kolejności. Kod przed wywołaniem i po nim pokazuje dwa różne przebiegi.

## Quicksort

Podziel elementy względem pivota na mniejsze, równe i większe. Sortuj rekurencyjnie części i połącz. Oddzielna część równych zachowuje powtórzenia i kończy przypadek wszystkich równych.

## LIFO

Stos działa ostatni wszedł, pierwszy wychodzi. Lista z append i pop realizuje taki porządek. Przed pop sprawdź pusty stos, jeśli aplikacja ma pokazać komunikat.

## FIFO

Kolejka obsługuje w kolejności przyjścia. deque.append dodaje na końcu, popleft pobiera z początku. Nie myl kolejności obsługi z sortowaniem po wartości zgłoszenia.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
