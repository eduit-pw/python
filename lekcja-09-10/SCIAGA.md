# Temat 05. Napisy i metody tekstowe

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `s[i], s[-1]` | Znak pod indeksem i ostatni znak | Indeks poza napisem powoduje IndexError. |
| `s[a:b:k]` | Wycinek od a do b bez b, co k znaków | Zbyt daleka granica wycinka jest dozwolona. |
| `s[::-1]` | Odwrócony napis | Zwraca nowy str. |
| `s.strip()` | Usunięcie białych znaków z brzegów | Nie usuwa spacji wewnętrznych. |
| `s.split(), s.split(";")` | Podział na listę napisów | Bez argumentu grupuje białe znaki. |
| `"-".join(elementy)` | Połączenie napisów separatorem | Elementy muszą być napisami. |
| `s.lower(), s.upper()` | Zmiana wielkości liter | Oryginał pozostaje bez zmian. |
| `s.replace("a", "b")` | Zamiana fragmentów | Wynik trzeba przypisać, jeśli ma zastąpić s. |
| `len(s), "x" in s` | Długość oraz obecność fragmentu | Wyniki: int oraz bool. |

## Krótki wzorzec

```python
tekst = "  kot;pies  "
slowa = tekst.strip().split(";")
print(" / ".join(slowa))  # kot / pies
print(tekst.strip()[1:3])  # ot
```

str jest niemodyfikowalny. s[0] = "A" powoduje TypeError. isdigit() rozpoznaje także niektóre cyfry spoza ASCII.

[Dokumentacja](https://docs.python.org/3.13/library/stdtypes.html#text-sequence-type-str) · [Zadania lekcji](README.md)
