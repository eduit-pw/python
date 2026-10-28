# Temat 07. Zakres nazw i elastyczne argumenty

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `x = ... wewnątrz funkcji` | Zwykle tworzy nazwę lokalną | Nie zmienia automatycznie x z modułu. |
| `global x` | Powiązanie przypisania z nazwą modułu | Często czytelniej zwrócić wynik. |
| `nonlocal x` | Nazwa z otaczającej funkcji | Nie dotyczy zmiennej globalnej. |
| `def f(x=10):` | Parametr z wartością domyślną | Wartość domyślna powstaje przy definicji funkcji. |
| `def f(*args):` | Dowolna liczba argumentów pozycyjnych | args jest krotką. |
| `def f(**kwargs):` | Dowolna liczba argumentów nazwanych | kwargs jest słownikiem. |
| `def f(*, tryb):` | Parametr wyłącznie nazwany | Wywołanie: f(tryb="krótki"). |
| `f(*lista), f(**slownik)` | Rozpakowanie argumentów | Gwiazdki przy wywołaniu rozpakowują dane. |

## Krótki wzorzec

```python
def dopisz(wartosc, dane=None):
    if dane is None:
        dane = []
    dane.append(wartosc)
    return dane

print(dopisz(2))  # [2]
print(dopisz(5))  # [5]
```

Domyślna lista w def f(dane=[]) jest współdzielona między wywołaniami korzystającymi z tego argumentu domyślnego. Wzorzec z None tworzy nową listę.

[Dokumentacja](https://docs.python.org/3.13/tutorial/controlflow.html#more-on-defining-functions) · [Zadania lekcji](README.md)
