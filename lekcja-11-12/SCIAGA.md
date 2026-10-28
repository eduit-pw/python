# Temat 06. Funkcje, argumenty i return

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `def nazwa(parametr):` | Definicja funkcji | Ciało wykonuje się po wywołaniu. |
| `nazwa(wartość)` | Wywołanie funkcji | Wartość trafia do parametru. |
| `return wynik` | Zwrócenie wyniku i koniec funkcji | Kończy także wykonanie pętli wewnątrz tej funkcji. |
| `print(wynik)` | Wyświetlenie wyniku | Sam print zwraca None. |
| `parametr=wartość` | Argument nazwany przy wywołaniu | Np. potega(podstawa=3, wykladnik=2). |
| `def f(x: int) -> int:` | Adnotacje typów | Same nie sprawdzają danych podczas wykonania. |
| `"""Opis funkcji."""` | Docstring | Pierwsza instrukcja wewnątrz funkcji. |
| `None` | Brak wartości wyniku | Funkcja bez wykonanego return też zwraca None. |

## Krótki wzorzec

```python
def pole_prostokata(a: float, b: float) -> float:
    """Zwraca iloczyn długości boków."""
    return a * b

wynik = pole_prostokata(3, b=4)
print(wynik)  # 12
```

Argumenty są wartościami podanymi przy wywołaniu, parametry to nazwy w definicji. Wynik obliczenia i jego wyświetlenie można rozdzielić.

[Dokumentacja](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions) · [Zadania lekcji](README.md)
