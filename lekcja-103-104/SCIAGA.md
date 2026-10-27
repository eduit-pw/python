# Temat 50. Wyjaśnienia do praktyki

## HTTP i żądanie

Klient wysyła metodę, adres, nagłówki i ewentualne ciało. Serwer zwraca status, nagłówki i treść. GET służy do odczytu, POST do przesłania danych zgodnie z umową API.

## Status i typ treści

200 oznacza poprawny odczyt, 201 utworzenie, 204 sukces bez treści. 404 dotyczy brakującego zasobu, a 500 błędu serwera. Content-Type określa format odpowiedzi, np. application/json.

## urlopen

urllib.request.urlopen pobiera odpowiedź i może otrzymać timeout. read daje bajty, decode tekst, json.loads strukturę. Dopiero potem kontrolujesz typ i pola danych.

## Rodzaje awarii

HTTPError opisuje błąd HTTP, URLError problem dostępu do zasobu. HTTPError jest podtypem URLError, więc obsłuż go wcześniej. Niepoprawny JSON ma osobny błąd parsowania.

## Umowa API

Dla operacji zapisz metodę, ścieżkę, wejście, sukces i błędy. Poprawne połączenie nie gwarantuje poprawnego schematu danych. Nie próbuj odczytywać JSON z pustej odpowiedzi 204.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
