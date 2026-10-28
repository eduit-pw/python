# Temat 02. Zmienne, typy i formatowanie

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `nazwa = wartość` | Przypisanie wartości do nazwy | = przypisuje, == porównuje. |
| `input("Komunikat: ")` | Pobranie wiersza z klawiatury | Wynik ma typ str. |
| `int("12"), float("2.5")` | Konwersja napisu na liczbę | Błędny zapis powoduje ValueError. |
| `str(12), type(12)` | Napis oraz odczyt typu | Odpowiednio "12" i int. |
| `bool(0), bool("")` | Konwersja do wartości logicznej | Oba wyniki to False. Niepusty napis "False" daje True. |
| `f"{cena:.2f}"` | Napis z dwoma miejscami po kropce | Formatowanie nie zmienia zmiennej cena. |
| `f"{numer:04d}"` | Dopełnienie liczby zerami | Dla 7 daje "0007". |
| `print(a, b, sep=";", end="!")` | Separator wartości i zakończenie | end zastępuje domyślny znak nowej linii. |

## Krótki wzorzec

```python
cena = 7.5
sztuki = 3
opis = f"Razem: {cena * sztuki:.2f} zł"
print(opis)  # Razem: 22.50 zł
```

Kody, numery telefonów i identyfikatory z zerem na początku przechowuj jako str. float używa przybliżeń binarnych.

[Dokumentacja](https://docs.python.org/3.13/tutorial/inputoutput.html) · [Zadania lekcji](README.md)
