# Temat 64. BeautifulSoup i HTML

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `BeautifulSoup(html, "html.parser")` | Parsowanie HTML | Biblioteka beautifulsoup4. |
| `soup.select(".karta")` | Wszystkie elementy pasujące do CSS | Wynik lista. |
| `soup.select_one("#tytul")` | Pierwszy pasujący element | Wynik Tag albo None. |
| `".klasa", "#id", "a[href]"` | Selektory klasy, ID i atrybutu | .klasa nie oznacza nazwy znacznika. |
| `element.get_text(strip=True)` | Tekst elementu | Opcjonalny separator=" " rozdziela fragmenty. |
| `element.get("href")` | Odczyt atrybutu | Zwraca None, gdy atrybutu nie ma. |
| `float(tekst.replace(",", "."))` | Przykładowa konwersja liczby | Wcześniej usuń symbole i sprawdź format danych. |
| `urllib.parse.urljoin(baza, href)` | Pełny adres z linku względnego | Sprawdź href przed łączeniem. |

## Krótki wzorzec

```python
from bs4 import BeautifulSoup

html = '<p class="cena">12,50 zł</p>'
soup = BeautifulSoup(html, "html.parser")
element = soup.select_one(".cena")
if element is not None:
    tekst = element.get_text(strip=True)
    wartosc = float(tekst.removesuffix(" zł").replace(",", "."))
    print(wartosc)  # 12.5
```

Parser nie wykonuje JavaScript. Brak elementu nie oznacza automatycznie wartości 0. Ustal, czy rekord pominąć, czy zgłosić błąd.

[Dokumentacja](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) · [Zadania lekcji](README.md)
