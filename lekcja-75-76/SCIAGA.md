# Temat 37. Rekurencja, stos i kolejka

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `Warunek bazowy` | Zakończenie rekurencji | Musi działać także dla najmniejszego dopuszczalnego wejścia. |
| `return f(mniejszy_problem)` | Przekazanie wyniku wywołania | Brak return może zgubić wynik. |
| `Stos wywołań` | Przechowywanie niezakończonych wywołań | Zbyt głęboka rekurencja może dać RecursionError. |
| `lista.append(x), lista.pop()` | Dodanie i zdjęcie ze stosu | LIFO: ostatni dodany wychodzi pierwszy. |
| `deque.append(x), deque.popleft()` | Dodanie i zdjęcie z kolejki | FIFO: pierwszy dodany wychodzi pierwszy. |
| `pivot oraz podział danych` | Idea quicksort | Równe elementy też muszą trafić do wyniku. |

## Krótki wzorzec

```python
from collections import deque

stos = []
stos.append("A")
stos.append("B")
print(stos.pop())  # B

kolejka = deque(["A", "B"])
print(kolejka.popleft())  # A
```

pop i popleft na pustej kolekcji zgłaszają IndexError. Quicksort ma średni koszt O(n log n), a w niekorzystnym przypadku O(n²).

[Dokumentacja](https://docs.python.org/3.13/library/collections.html#collections.deque) · [Zadania lekcji](README.md)
