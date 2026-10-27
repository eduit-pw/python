# Temat 61. Wyjaśnienia do praktyki

## Obraz i kontener

Obraz opisuje środowisko i pliki aplikacji. Kontener jest uruchomioną instancją obrazu. Zmiana źródeł wymaga przebudowania obrazu, jeśli nie montujesz ich jako osobnego zasobu.

## Dockerfile

FROM wybiera bazę, WORKDIR katalog pracy, COPY pliki, RUN wykonuje instalację podczas budowy, CMD wskazuje start przy uruchomieniu. Nie myl budowy ze startem aplikacji.

## Porty

-p 127.0.0.1:8000:8000 udostępnia port kontenera lokalnie na hoście. Uvicorn wewnątrz powinien nasłuchiwać na 0.0.0.0. Adres 127.0.0.1 wewnątrz kontenera ma inne znaczenie niż na hoście.

## Wolumen

Nazwany wolumen przechowuje dane niezależnie od usunięcia kontenera. Ścieżka bazy musi trafiać do zamontowanego katalogu. Usunięcie wolumenu usuwa tę kopię danych.

## Diagnostyka

docker ps -a pokazuje także zatrzymane kontenery, docker logs komunikaty startu. Błędny moduł main:app uniemożliwi start mimo udanej budowy obrazu. .dockerignore ogranicza pliki przekazywane do budowy.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
