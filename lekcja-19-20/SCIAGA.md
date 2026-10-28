# Temat 10. Słowniki

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `d = {"klucz": wartość}` | Powiązanie klucza z wartością | Klucze muszą być hashowalne. |
| `d[klucz]` | Odczyt wartości | Brak klucza powoduje KeyError. |
| `d.get(klucz, domyslna)` | Odczyt z wartością zastępczą | Nie dodaje brakującego wpisu. |
| `d[klucz] = wartość` | Dodanie lub zastąpienie wartości | Istniejący klucz pozostaje jednym kluczem. |
| `klucz in d` | Sprawdzenie obecności klucza | Nie sprawdza wartości. |
| `d.keys(), d.values(), d.items()` | Widoki kluczy, wartości i par | items daje pary do rozpakowania. |
| `d.pop(klucz, domyslna)` | Usunięcie i zwrot wartości | Wartość domyślna obsługuje brak wpisu. |
| `d.update(inny)` | Dodanie lub zastąpienie wielu wpisów | Modyfikuje d. |

## Krótki wzorzec

```python
ceny = {"chleb": 5, "mleko": 4}
ceny["woda"] = 2
for produkt, cena in ceny.items():
    print(produkt, cena)
print(ceny.get("ryż", 0))  # 0
```

for x in d przechodzi po kluczach. Słownik zachowuje kolejność wstawiania, ale nie sortuje kluczy.

[Dokumentacja](https://docs.python.org/3.13/library/stdtypes.html#mapping-types-dict) · [Zadania lekcji](README.md)
