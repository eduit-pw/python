# Temat 40. Wyjaśnienia do praktyki

## Plik .ui

Designer zapisuje strukturę interfejsu w XML .ui. objectName pozwala odszukać kontrolkę w kodzie. Tekst widoczny na przycisku i objectName są różnymi właściwościami.

## Layout w Designer

Layout określa rozmieszczenie przy zmianie rozmiaru. Umieść kontrolki w układzie, a potem sprawdź podgląd. Ręczne pozycje nie zapewniają dopasowania do różnych rozmiarów.

## loadUi

PyQt6.uic.loadUi wczytuje .ui w czasie wykonania. Plik musi być dostępny w paczce. Ścieżkę buduj względem skryptu, żeby katalog terminalu nie zmieniał wyniku.

## Generowanie kodu

python -m PyQt6.uic.pyuic okno.ui -o ui_okno.py tworzy kod interfejsu. Po zmianie .ui wygeneruj go ponownie. Logikę aplikacji trzymaj w osobnym własnym pliku.

## Połączenie akcji

clicked.connect(self.powitaj) przekazuje metodę do wykonania po kliknięciu. Nawiasy self.powitaj() uruchomiłyby ją od razu. W metodzie pobierz text, zastosuj strip i ustaw wynik.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
