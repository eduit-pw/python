# Diagnozowanie i usuwanie błędów w kodzie aplikacji z wykorzystaniem debuggera i testów jednostkowych

**Temat 36. Lekcje 71-72. Czas: 90 minut.**

## Po tej lekcji

- Przeczytam traceback i wskażę przyczynę wyjątku.
- Prześledzę wartości zmiennych i stos wywołań w debuggerze.
- Napiszę test regresyjny sprawdzający wynik i stan po błędzie.

## Praca w bloku

| Czas | Działanie |
| --- | --- |
| 0–20 min | Prezentacja, krótka demonstracja i pytania teoretyczne. |
| 20–35 min | Zadanie 1 z prowadzącym. |
| 35–55 min | Zadanie 2 w parach lub wspólnie. |
| 55–80 min | Zadanie 3 samodzielnie, kontrola wyniku. |
| 80–90 min | Omówienie, zapis pracy i krótkie pytania. |

Zadanie 4 jest dla osób, które ukończą podstawę wcześniej, albo do samodzielnej kontynuacji. Diagnoza jest materiałem zapasowym i do pracy własnej. Nie jest dodatkowym obowiązkowym etapem bloku.

## Przygotowanie stanowiska

Potrzebujesz Pythona 3.10 lub nowszego, VS Code z rozszerzeniami Python i Python Debugger oraz wybranego interpretera. Nauczyciel sprawdza zgodność interpretera i rozszerzeń przed zajęciami. Wystarcza biblioteka standardowa. Skróty odnoszą się do standardowych ustawień VS Code na Windows; te same akcje są w menu Run i na pasku debuggera.

Otwórz w VS Code dokładnie folder `lekcja-71-72`. Utwórz w nim `praca` i skopiuj do niego pliki z `startery`. To właśnie pliki w `praca` będziesz poprawiać. Zapisuj plik przed uruchomieniem. Polecenia wykonuj z folderu `praca`. W razie potrzeby użyj `python3` albo `py` zamiast `python`.

W pliku `.vscode/launch.json` są trzy gotowe konfiguracje. Wybierz je w widoku Run and Debug. W [KONSTRUKCJE.md](KONSTRUKCJE.md) znajdziesz skróty i krótkie wzorce.

Startery zawierają celowe błędy. Początkowe niepowodzenia testów są częścią ćwiczenia. Nie zmieniaj oczekiwanych wyników tak, aby dopasować je do błędnego programu.

## Zadanie 1. Traceback i indeks poza listą

1. Uruchom `python dane.py`. Przeczytaj ostatnią linię tracebacku, następnie znajdź plik i linię własnego kodu, w której wystąpił błąd.
2. Funkcja `ostatni_element(wartosci)` ma zwracać ostatni element niepustej listy, a dla pustej zgłaszać `ValueError`.
3. Sprawdź związek między długością listy `[4, 7, 9]` a indeksem jej ostatniego elementu. Popraw kod.
4. Uruchom `python -m unittest test_dane -v`. Mają przejść dwa testy: wynik `9` oraz odrzucenie pustej listy.

Zapisz krótko: typ błędu, przyczyna i poprawka. Nie dopisuj ogólnego `except Exception`, które ukrywa wadę funkcji.

## Zadanie 2. Debugger wykrywa błędny rabat

**Kontrakt:** `cena_po_rabacie(cena_grosze, procent)` przyjmuje nieujemną cenę w groszach i rabat od 0 do 100. Argumenty są liczbami całkowitymi. Rabat w groszach obliczamy jako `cena_grosze * procent // 100`, a następnie odejmujemy go od ceny. Ewentualną część ułamkową rabatu odrzucamy.

1. W `rabaty.py` ustaw punkt przerwania przy instrukcji wyliczającej `rabat`.
2. Wybierz konfigurację „Rabat: plik ćwiczeniowy” i rozpocznij debugowanie przez F5.
3. W panelu Variables obejrzyj `cena_grosze` i `procent`. Debugger zatrzymał się przed wykonaniem oznaczonej instrukcji.
4. Przejdź o krok przez F10. Odczytaj `rabat`, następnie wykonaj kolejną instrukcję i odczytaj `wynik`.
5. Porównaj wartości rzeczywiste z tabelą, popraw przyczynę błędu i powtórz próbę.

| Dane | Poprawny rabat | Poprawna cena końcowa |
| --- | ---: | ---: |
| 20000 groszy, 15% | 3000 | 17000 |
| 20000 groszy, 0% | 0 | 20000 |
| 20000 groszy, 100% | 20000 | 0 |

Uruchom `python -m unittest test_rabaty -v`: oczekuj trzech testów i `OK`. Zapisz jeden wiersz obserwacji przed poprawką i jeden po niej.

## Zadanie 3. Wyjątek wystąpił, ale stan obiektu jest błędny

**Kontrakt:** `RezerwacjaMiejsc(wolne)` przechowuje nieujemną liczbę wolnych miejsc. `zarezerwuj(liczba)` przyjmuje dodatnią liczbę całkowitą. Poprawna rezerwacja zmniejsza stan. Rezerwacja większa niż dostępny stan powoduje `ValueError` i pozostawia dotychczasową liczbę miejsc. Rezerwacja 0 lub wartości ujemnej również powoduje `ValueError`.

1. W `test_rezerwacje.py` napisz dwa testy:
   - dla początkowego stanu `5` rezerwacja `2` pozostawia `3`;
   - dla początkowego stanu `5` rezerwacja `6` zgłasza `ValueError`, po którym nadal jest `5` wolnych miejsc.
2. Uruchom `python -m unittest test_rezerwacje -v`. Drugi test powinien ujawnić błąd startera. Umieść sprawdzenie stanu po bloku `with self.assertRaises(ValueError):`.
3. Ustaw punkt przerwania w `zarezerwuj`. Wybierz konfigurację „Rezerwacja: testy ćwiczeniowe”. Obserwuj `liczba` i `self.wolne`, także w odrzuconej próbie.
4. Popraw kolejność sprawdzeń i zmiany stanu. Uruchom oba testy ponownie.
5. Wykonaj `python -m unittest discover -v`: podstawowy komplet ma obejmować **7 testów** i zakończyć się `OK`.

## Zadanie 4. Dla chętnych: warunkowy punkt przerwania

W poprawionym `rabaty.py` ustaw punkt przerwania przy obliczaniu rabatu. W jego ustawieniach wpisz warunek `procent == 100`. Uruchom konfigurację „Serie: warunkowy punkt przerwania”.

Sprawdź, przy której z trzech prób nastąpi zatrzymanie i jakie wartości mają argumenty. Użyj stosu wywołań, aby wskazać funkcję, która wywołała `cena_po_rabacie`. Po demonstracji usuń warunek albo wyłącz punkt przerwania.

## Diagnoza do samodzielnej pracy

W [diagnoza/napraw.py](diagnoza/napraw.py) funkcja średniej zwraca dla `[2, 3]` wynik `2`, choć kontrakt wymaga `2.5`. Napraw operator i z folderu `diagnoza` uruchom `python sprawdz.py`. Oczekuj dwóch testów i `OK`.

## Zakończenie

Pokaż poprawny wynik wszystkich 7 testów. W komentarzach w swoim `rabaty.py` zapisz zaobserwowaną przyczynę błędu i sposób sprawdzenia poprawki. Wyjaśnij, dlaczego zgłoszenie wyjątku nie przywróciło automatycznie stanu rezerwacji. Rozwiązania porównawcze są w [rozwiazania](rozwiazania/).

## Źródła

- [Microsoft: Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging).
- [Microsoft: ogólne funkcje debuggera](https://code.visualstudio.com/docs/debugtest/debugging).
- [Python: unittest i asercje](https://docs.python.org/3/library/unittest.html).

Dostęp: 4 listopada 2026 r. Polecenia i przykłady przygotowano dla tej lekcji.
