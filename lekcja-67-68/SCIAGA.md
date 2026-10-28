# Temat 33. Liczby pierwsze, sito i NWD

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `n < 2` | Wykluczenie liczby pierwszej | 0, 1 i liczby ujemne nie są pierwsze. |
| `d * d <= n` | Granica prób dzielenia | Trzeba uwzględnić dzielnik równy pierwiastkowi. |
| `n % d == 0` | Sprawdzenie podzielności | d musi być różne od 0. |
| `[True] * (n + 1)` | Tablica znaczników od 0 do n | Znaczniki 0 i 1 trzeba wyłączyć. |
| `range(p * p, n + 1, p)` | Wielokrotności w sicie | Niższe wielokrotności p już mają mniejszy dzielnik. |
| `n //= d` | Usunięcie jednego czynnika | Dla powtarzającego się czynnika wykonuj wielokrotnie. |
| `a, b = b, a % b` | Krok algorytmu Euklidesa | Powtarzaj, dopóki b != 0. |
| `math.gcd(a, b), math.isqrt(n)` | Gotowe NWD i pierwiastek całkowity | Przydatne do kontroli własnego rozwiązania. |

## Krótki wzorzec

```python
import math

n = 49
print(math.isqrt(n))  # 7
print(n % 7 == 0)     # True
print(math.gcd(30, 42))  # 6
```

Jeśli zadanie wymaga konkretnego algorytmu, pokaż jego kroki. math.gcd może sprawdzić wynik, ale nie zastąpi wymaganego kodu.

[Dokumentacja](https://docs.python.org/3.13/library/math.html) · [Zadania lekcji](README.md)
