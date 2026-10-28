# Temat 31. Systemy liczbowe i Horner

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `int(tekst, podstawa)` | Zamiana zapisu na int | int("101", 2) daje 5. |
| `bin(n), oct(n), hex(n)` | Zapis binarny, ósemkowy i szesnastkowy | Wynik str z prefiksem 0b, 0o lub 0x. |
| `format(n, "b"), format(n, "X")` | Zapis bez prefiksu | "b" binarnie, "X" szesnastkowo dużymi literami. |
| `divmod(n, podstawa)` | Iloraz i reszta | Zwraca krotkę (n // podstawa, n % podstawa). |
| `wynik = wynik * p + cyfra` | Krok Hornera dla podstawy p | Cyfry przetwarzaj od lewej strony. |
| `wynik = wynik * x + wspolczynnik` | Krok Hornera dla wielomianu | Współczynniki od najwyższej potęgi. |
| `0 <= cyfra < podstawa` | Warunek poprawnej cyfry | Dla systemu dwójkowego tylko 0 i 1. |

## Krótki wzorzec

```python
zapis = "120"
wynik = 0
for znak in zapis:
    wynik = wynik * 3 + int(znak)
print(wynik)          # 15
print(int(zapis, 3))  # 15
print(format(15, "b"))  # 1111
```

W wielomianie uwzględnij współczynniki zerowe brakujących potęg. Gdy polecenie wymaga własnego algorytmu, gotowa konwersja nie zastępuje jego implementacji.

[Dokumentacja](https://docs.python.org/3.13/library/functions.html#int) · [Zadania lekcji](README.md)
