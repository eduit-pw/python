# Konstrukcje: debugger i test regresyjny

| Akcja w VS Code | Standardowy skrót Windows | Zastosowanie |
| --- | --- | --- |
| Start / Continue | F5 | Start debuggera lub wznowienie wykonania. |
| Toggle Breakpoint | F9 | Dodanie lub usunięcie punktu przerwania. |
| Step Over | F10 | Wykonanie bieżącej instrukcji bez przechodzenia krokowo przez funkcję. |
| Step Into | F11 | Wejście do wywoływanej funkcji, jeśli debugger pozwala śledzić jej kod. |
| Step Out | Shift+F11 | Wykonanie reszty funkcji i powrót do wywołującego. |
| Stop | Shift+F5 | Zakończenie sesji debugowania. |

Przy innych skrótach użyj nazw akcji z menu Run. Debugger zatrzymuje się przed wykonaniem bieżącej instrukcji. W panelu Variables odczytasz lokalne wartości, w Watch dodasz wyrażenie, a Call Stack pokazuje łańcuch wywołań. Do obserwacji wybieraj wyrażenia bez zmiany stanu, np. `self.wolne`.

Warunkowy punkt przerwania ustawiasz przez jego menu kontekstowe. Przykład warunku: `procent == 100`.

```python
with self.assertRaises(ValueError):
    rezerwacja.zarezerwuj(6)
self.assertEqual(rezerwacja.wolne, 5)
```

Pierwsza asercja sprawdza wyjątek, druga stan obiektu po zakończeniu bloku. Nie umieszczaj sprawdzenia stanu po instrukcji zgłaszającej wyjątek wewnątrz tego samego bloku.

```text
python -m unittest test_rabaty -v
python -m unittest discover -v
```

**FAIL:** niezgodność sprawdzana przez asercję. **ERROR:** nieoczekiwany wyjątek podczas przygotowania lub wykonania testu. Oczekiwany wyjątek wewnątrz właściwego `assertRaises` jest poprawnym wynikiem testu.

**Kolejność diagnozy:** odtwórz problem na znanych danych, przeczytaj błąd, sprawdź wartości, popraw przyczynę i powtórz test. Zachowaj niezależny wynik oczekiwany. Zmiana oczekiwania na błędny wynik programu ukrywa problem.

## Dokumentacja

- [Microsoft: Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging).
- [Microsoft: ogólne funkcje debuggera](https://code.visualstudio.com/docs/debugtest/debugging).
- [Python: unittest i asercje](https://docs.python.org/3/library/unittest.html).

Dostęp: 4 listopada 2026 r. Polecenia i przykłady przygotowano dla tej lekcji.
