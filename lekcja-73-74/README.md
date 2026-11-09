# Wersjonowanie kodu w systemie Git: zapisywanie zmian, przeglądanie historii i przywracanie plików

**Temat 37. Lekcje 73-74. Czas: 90 minut.**

## Po tej lekcji

- Utworzę lokalne repozytorium i zapiszę dwie wersje programu.
- Rozróżnię zmiany robocze, indeks i historię commitów.
- Przywrócę wskazany plik i wyjaśnię działanie .gitignore.

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

Potrzebujesz Pythona 3.8 lub nowszego oraz Git w wersji co najmniej 2.23, która udostępnia `git restore`. Nauczyciel sprawdza przed zajęciami `git --version` i dostępność Git w terminalu. Konta w serwisach internetowych nie są potrzebne.

Utwórz nowy, pusty folder `git-lab-37` poza pobranym repozytorium kursu. Skopiuj do niego zawartość `startery`, w tym `.gitignore`. Otwórz ten folder w VS Code lub innym edytorze. Wszystkie poniższe polecenia wykonuj z `git-lab-37`. Polecenie `git init` dotyczy wyłącznie tego nowego katalogu. W razie potrzeby zamiast `python` używaj `python3` albo `py`.

Ćwiczymy na przygotowanych kopiach. Polecenie `git restore -- program.py` zastępuje niezapisane w indeksie zmiany tego pliku wersją z indeksu. Przed przywróceniem obejrzyj różnice i upewnij się, że chcesz odrzucić właśnie ćwiczeniową zmianę.

Przydatne polecenia i znaczenie flag znajdziesz w [KONSTRUKCJE.md](KONSTRUKCJE.md).

## Zadanie 1. Pierwszy zapis wersji

1. W terminalu sprawdź wersje i utwórz repozytorium:

```text
python --version
git --version
git init
git config user.name "Uczen"
git config user.email "uczen@example.invalid"
```

Konfiguracja jest lokalna dla ćwiczeniowego repozytorium. Wartości to fikcyjne dane do nauki.

2. Otwórz `.gitignore`. Powinien zawierać:

```gitignore
.venv/
__pycache__/
*.pyc
lokalne.txt
```

3. Utwórz w edytorze `lokalne.txt` z dowolną notatką i uruchom test. Sprawdź status, a następnie zapisz pierwszą wersję:

```text
python -m unittest discover -v
git status
git add .gitignore program.py test_program.py
git status
git commit -m "Pierwsza wersja powitania"
git log --oneline
```

Oczekuj jednego wykonanego testu, jednego commita i braku `lokalne.txt` oraz `__pycache__` wśród zmian do zapisu. Nazwa domyślnej gałęzi i identyfikator commita mogą być inne na poszczególnych komputerach.

## Zadanie 2. Zmiana kodu i testu, drugi commit

1. W `program.py` zmień funkcję tak, aby usuwała spacje z brzegów imienia:

```python
def przywitanie(imie):
    return f"Cześć, {imie.strip()}!"
```

2. W istniejącej klasie testowej dodaj drugą metodę:

```python
    def test_spacje(self):
        self.assertEqual(przywitanie("  Ala  "), "Cześć, Ala!")
```

3. Zapisz oba pliki. Wykonaj polecenia w tej kolejności:

```text
python -m unittest discover -v
git diff
git add program.py test_program.py
git diff
git diff --staged
git commit -m "Usuniecie spacji z imienia"
git log --oneline
```

Oczekuj dwóch testów i `OK`, a w historii dwóch commitów. Po `git add` zwykły `git diff` ma być pusty, jeśli nie edytowałeś plików ponownie. `git diff --staged` pokazuje przygotowane zmiany względem ostatniego commita. Commit zapisuje stan przygotowany w indeksie.

## Zadanie 3. Przywracanie pliku i cofnięcie przygotowania zmiany

### A. Zmiana tylko w pliku roboczym

Zmień wynik funkcji `przywitanie` na stały napis `"BLAD"` i zapisz plik. Nie wykonuj `git add`. Uruchom testy i obejrzyj różnice, a następnie przywróć plik:

```text
python -m unittest discover -v
git diff -- program.py
git restore -- program.py
python -m unittest discover -v
git status
```

Przed przywróceniem oba testy zawodzą, po nim oba przechodzą. Przywrócenie dotyczy wskazanego pliku. Ostatni commit pozostaje bez zmian.

### B. Błędna zmiana trafiła do indeksu

Ponownie zmień zwracany napis na `"BLAD"`, zapisz plik i wykonaj `git add program.py`. Teraz wykonaj:

```text
git diff
git diff --staged -- program.py
git restore --staged -- program.py
git diff -- program.py
git restore -- program.py
python -m unittest discover -v
git status
```

Po `restore --staged` błędna zmiana nadal jest w pliku roboczym, ale znika z indeksu. Dopiero następne `restore` przywraca plik z indeksu. Na końcu testy przechodzą, status nie pokazuje zmian do zapisu, a historia nadal zawiera dwa commity.

## Zadanie 4. Dla chętnych: wcześniejsza wersja jednego pliku

Wykonuj to przy czystym statusie po zadaniu 3. Najpierw obejrzyj dawną treść, następnie przywróć ją tylko do pliku roboczego:

```text
git show HEAD~1:program.py
git restore --source=HEAD~1 -- program.py
python -m unittest discover -v
git diff -- program.py
git restore -- program.py
python -m unittest discover -v
```

Starsza wersja nie usuwa spacji, więc nowy test `test_spacje` zgłasza `FAIL`. Po powrocie do wersji z indeksu oba testy przechodzą. Nie tworzysz nowego commita i nie przesuwasz gałęzi. `HEAD~1` oznacza w tym liniowym przykładzie rodzica aktualnego commita.

## Diagnoza do samodzielnej pracy

Uczeń zmienił plik, wykonał `git add`, a potem uruchomił `git diff` i zobaczył pusty wynik. Wyjaśnij przyczynę i wskaż polecenie pokazujące przygotowaną zmianę. Drugie pytanie: dlaczego dopisanie śledzonego już pliku do `.gitignore` nie przestaje go automatycznie śledzić?

## Zakończenie

Pokaż `git log --oneline`, czysty status i wynik dwóch testów. Ustnie wyjaśnij różnicę między plikiem roboczym, indeksem i commitem. Lokalne repozytorium ma zawierać własne wykonane commity. Pliki w [rozwiazania](rozwiazania/) pokazują treść obu wersji, a nie gotową historię Git.

## Źródła

- [Pro Git: zapisywanie zmian w repozytorium](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository).
- [Git: restore](https://git-scm.com/docs/git-restore).
- [Git: diff](https://git-scm.com/docs/git-diff).
- [Git: gitignore](https://git-scm.com/docs/gitignore).

Dostęp: 4 listopada 2026 r. Polecenia i przykłady przygotowano dla tej lekcji.
