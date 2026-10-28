# Temat 25. Wzorce i dekoratory

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `__new__(cls)` | Utworzenie instancji | Może służyć do kontrolowania jednej instancji. |
| `__init__(self)` | Inicjalizacja instancji | Może uruchomić się ponownie po zwrocie istniejącego obiektu z __new__. |
| `Metoda wytwórcza` | Punkt tworzenia obiektu | Pozwala podklasie zmienić typ tworzonego produktu. |
| `@dekorator` | Opakowanie funkcji podczas definicji | Odpowiada przypisaniu f = dekorator(f). |
| `def wrapper(*args, **kwargs):` | Przekazanie dowolnych argumentów | Funkcja wewnętrzna wywołuje oryginał. |
| `return funkcja(*args, **kwargs)` | Przekazanie wyniku oryginału | Brak return zgubiłby wynik. |
| `return wrapper` | Zwrócenie opakowania z dekoratora | Bez nawiasów. |
| `@functools.wraps(funkcja)` | Zachowanie metadanych oryginału | M.in. __name__ i docstring. |

## Krótki wzorzec

```python
from functools import wraps

def z_opisem(funkcja):
    @wraps(funkcja)
    def wrapper(*args, **kwargs):
        wynik = funkcja(*args, **kwargs)
        return f"Wynik: {wynik}"
    return wrapper

@z_opisem
def podwoj(x):
    return x * 2

print(podwoj(4))  # Wynik: 8
```

Singleton w prostym przykładzie nie rozwiązuje automatycznie problemów wielu wątków i procesów. Wzorzec dobieraj do potrzeby, nie do samej nazwy.

[Dokumentacja](https://docs.python.org/3.13/library/functools.html#functools.wraps) · [Zadania lekcji](README.md)
