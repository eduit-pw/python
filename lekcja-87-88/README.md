# Ćwiczenia: Układanie elementów w oknie: rozmieszczenie pionowe, poziome i dopasowanie do rozmiaru ekranu

**Temat 43 | Lekcje 87-88**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Organizacja okna

Każde zadanie zapisz jako osobny program, zachowując wersje wcześniejsze. W zadaniu 1 przycisk „Pokaż” kopiuje przycięty tekst pola do etykiety; pusty tekst daje „Podaj imię”. Zadanie 2 ćwiczy rozmieszczenie i nie wymaga zapisu danych. W zadaniu 3 podpisy R, G, B i odpowiadające im suwaki mają tworzyć trzy kolumny; podgląd jest w kolejnym wierszu, z columnSpan=3. Zakres suwaków 0-255, zmiany odświeżają kolor.

## Zadanie 1. Pionowy formularz

- Utwórz QWidget, QLineEdit, QPushButton „Pokaż” i QLabel.
- Umieść je w QVBoxLayout, odstęp 12 i marginesy po 20.
- Ustaw rozmiar 500 na 300. Sprawdź także 800 na 450.

**Wynik kontrolny:** kolejność kontrolek zachowana, pola wykorzystują dostępne miejsce.

## Zadanie 2. Formularz i przyciski

- Dodaj QFormLayout z polami Imię i Klasa oraz dolny QHBoxLayout.
- W dolnym układzie umieść stretch, „Zapisz” i „Anuluj”.
- Sprawdź widoczność etykiet przy wąskim i szerokim oknie.

**Wynik kontrolny:** etykiety w kolumnie, oba przyciski przy prawym brzegu.

## Zadanie 3. Siatka RGB

- Ułóż trzy podpisane suwaki RGB w jednym wierszu QGridLayout.
- Pod nimi umieść podgląd obejmujący wszystkie trzy kolumny.
- Nadaj podglądowi minimalną wysokość 120. Sprawdź zmianę rozmiaru.

**Wynik kontrolny:** trzy kolumny suwaków, szeroki podgląd pod nimi.

## Zadanie 4. QMainWindow bez nakładania

- Przenieś układ zadania 2 do QMainWindow przez centralny QWidget.
- Ustal minimalny rozmiar 400 na 250. Sprawdź większy rozmiar.
- Usuń ręczne move i setGeometry dla kontrolek obsługiwanych przez układ.

**Wynik kontrolny:** kontrolki bez nakładania i bez wychodzenia poza obszar centralny.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
