# Temat 03. Operatory i warunki

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `a / b` | Dzielenie | Dla liczb int daje float. |
| `a // b` | Iloraz zaokrąglony w dół | 7 // 3 to 2, a -7 // 3 to -3. |
| `a % b` | Reszta zgodna z dzieleniem // | 7 % 3 to 1. |
| `a ** b` | Potęgowanie | 2 ** 3 to 8. |
| `==, !=, <, <=, >, >=` | Porównania | Zwykle dają True albo False. |
| `dol <= x <= gora` | Sprawdzenie przedziału domkniętego | Obie granice należą do przedziału. |
| `and, or, not` | Łączenie i negowanie warunków | and i or stosują skrócone obliczanie. |
| `if / elif / else` | Wybór gałęzi | Wykonuje się pierwsza pasująca gałąź. |

## Krótki wzorzec

```python
liczba = 47
print(liczba // 10, liczba % 10)  # 4 7
if 10 <= liczba < 50:
    print("W przedziale")
else:
    print("Poza przedziałem")
```

Dwa osobne if mogą wykonać dwa bloki. W łańcuchu if/elif/else wykona się najwyżej jeden. Zero jako dzielnik powoduje ZeroDivisionError.

[Dokumentacja](https://docs.python.org/3.13/tutorial/controlflow.html) · [Zadania lekcji](README.md)
