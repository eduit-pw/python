# Temat 32. Operacje przy szyfrowaniu tekstu

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `ord(znak)` | Kod znaku Unicode | Argument musi mieć długość 1. |
| `chr(kod)` | Znak o wskazanym kodzie | Operacja odwrotna do ord w prawidłowym zakresie. |
| `ord(znak) - ord("A")` | Indeks litery A..Z | Zakres sprawdź przed obliczeniem. |
| `(indeks + klucz) % 26` | Przesunięcie w alfabecie 26 liter | Modulo zawija indeks na początek. |
| `(indeks - klucz) % 26` | Przesunięcie odwrotne | Przydatne przy odszyfrowaniu. |
| `slownik.get(znak, znak)` | Podstawienie lub zachowanie znaku | Mapa może obsługiwać pary zamian. |
| `"".join(znaki)` | Składanie wyniku z fragmentów | Zwraca str. |

## Krótki wzorzec

```python
znak = "Y"
klucz = 4
indeks = ord(znak) - ord("A")
nowy = chr(ord("A") + (indeks + klucz) % 26)
print(nowy)  # C
```

Ten przykład dotyczy tylko A..Z. Małe litery, polskie znaki i znaki spoza alfabetu wymagają jawnej reguły. Proste szyfry szkolne nie chronią poufnych danych.

[Dokumentacja](https://docs.python.org/3.13/library/functions.html#ord) · [Zadania lekcji](README.md)
