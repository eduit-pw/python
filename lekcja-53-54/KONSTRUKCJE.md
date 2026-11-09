# Konstrukcje: moduły i importy

| Zapis | Co udostępnia lub uruchamia? | Przykład użycia |
| --- | --- | --- |
| `import narzedzia` | Nazwę modułu. | `narzedzia.podwoj(3)` |
| `from narzedzia import podwoj` | Wybraną nazwę. | `podwoj(3)` |
| `import narzedzia as n` | Moduł pod lokalnym aliasem. | `n.podwoj(3)` |
| `from model import Notatka` | Klasę z sąsiedniego modułu. | `Notatka("Plan")` |
| `__name__` | Nazwę bieżącego modułu lub `"__main__"`. | Warunek punktu wejścia. |
| `python main.py` | Wskazany skrypt. | Wykonuj z folderu projektu. |
| `python -m notatki.main` | Moduł odszukany w pakiecie. | Wykonuj z folderu zawierającego `notatki`. |
| `python -m unittest discover -v` | Odkrywanie i wykonanie testów. | Nazwy plików `test*.py`, metod `test_...`. |

```python
def main():
    print("Uruchomiono menu")


if __name__ == "__main__":
    main()
```

Import modułu wykonuje jego instrukcje na najwyższym poziomie. Warunek powyżej chroni wyłącznie umieszczone w nim wywołanie. W zwykłym przebiegu interpreter przechowuje zaimportowane moduły i nie wykonuje ich kodu ponownie przy każdym kolejnym imporcie.

`__init__.py` oznacza używany na lekcji zwykły pakiet. Plik może być pusty. Python obsługuje także inne rodzaje pakietów, których ten blok nie wymaga.

**Praktyczne pułapki:** unikaj nazw własnych plików takich jak `random.py`, `json.py` lub `unittest.py`. Mogą zasłonić moduły standardowe. Przy `ModuleNotFoundError` sprawdź nazwę pliku, strukturę katalogów i folder uruchomienia. `ImportError` dotyczący konkretnej nazwy może wskazywać na literówkę, brak definicji lub cykl importów.

**Podział ról:** model przechowuje dane, logika wykonuje operacje, menu obsługuje klawiaturę i komunikaty. Test importuje model lub logikę.

## Dokumentacja

- [Python: moduły i pakiety](https://docs.python.org/3/tutorial/modules.html).
- [Python: punkt wejścia __main__](https://docs.python.org/3/library/__main__.html).
- [Python: unittest, discovery i asercje](https://docs.python.org/3/library/unittest.html).

Dostęp: 4 listopada 2026 r. Polecenia i przykłady przygotowano dla tej lekcji.
