# Temat 04. Pętle i sterowanie wykonaniem

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `range(stop)` | Liczby od 0 do stop bez stop | range(3) daje kolejno 0, 1, 2. |
| `range(start, stop, krok)` | Zakres z określonym krokiem | range(5, 0, -2) daje 5, 3, 1. |
| `for element in dane:` | Przejście po elementach | Pusty zakres oznacza zero iteracji. |
| `while warunek:` | Powtarzanie, dopóki warunek jest prawdziwy | Zadbaj o zmianę stanu pętli. |
| `break` | Zakończenie najbliższej pętli | Nie kończy automatycznie pętli zewnętrznej. |
| `continue` | Pominięcie reszty bieżącej iteracji | W while może ominąć zmianę licznika. |
| `suma += liczba` | Aktualizacja akumulatora | Zwykle suma zaczyna się od 0. |
| `licznik += 1` | Zliczenie jednego przypadku | Zwiększaj dopiero po spełnieniu warunku. |

## Krótki wzorzec

```python
suma = 0
for liczba in range(2, 9, 2):
    suma += liczba
print(suma)  # 20
```

Górna granica range nie należy do zakresu. Warunek while jest sprawdzany przed każdym obiegiem, także przed pierwszym.

[Dokumentacja](https://docs.python.org/3.13/tutorial/controlflow.html) · [Zadania lekcji](README.md)
