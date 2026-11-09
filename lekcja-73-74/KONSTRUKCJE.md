# Konstrukcje: Git w lokalnym projekcie

Wykonuj polecenia w przygotowanym folderze `git-lab-37`.

| Polecenie | Działanie |
| --- | --- |
| `git init` | Tworzy repozytorium w bieżącym folderze. |
| `git config user.name "Uczen"` | Ustawia autora lokalnie dla tego repozytorium. |
| `git status` | Pokazuje stan plików i indeksu. |
| `git add program.py` | Przygotowuje aktualną treść wskazanego pliku w indeksie. |
| `git diff` | Porównuje pliki robocze z indeksem. |
| `git diff --staged` | Porównuje indeks z ostatnim commitem. |
| `git commit -m "Opis zmiany"` | Zapisuje przygotowaną wersję w historii. |
| `git log --oneline` | Pokazuje zwięzłą historię commitów. |
| `git restore -- program.py` | Zastępuje roboczą treść pliku treścią z indeksu. |
| `git restore --staged -- program.py` | Przywraca indeks domyślnie ze stanu HEAD, zachowując plik roboczy. |
| `git show HEAD~1:program.py` | Wyświetla dawną treść pliku w liniowej historii ćwiczenia. |
| `git restore --source=HEAD~1 -- program.py` | Kopiuje dawną wersję do pliku roboczego, pozostawiając indeks. |

`HEAD` wskazuje aktualnie wybraną wersję. W tej lekcji pozostajemy na jednej gałęzi. `HEAD~1` jest rodzicem bieżącego commita. Część `--` oddziela opcje od ścieżek plików.

Po `git add` i dalszej edycji pliku możesz mieć jednocześnie zmianę przygotowaną i zmianę roboczą. Commit zapisze wersję z indeksu.

```gitignore
.venv/
__pycache__/
*.pyc
lokalne.txt
```

Reguły `.gitignore` nie przestają automatycznie śledzić plików obecnych w indeksie. Samo usunięcie pliku roboczego też nie usuwa jego wcześniejszych wersji z historii.

Przywracanie zastępuje wskazaną treść. Najpierw użyj `status` i odpowiedniego `diff`, a ćwiczenia wykonuj na przygotowanej kopii. Nazwy gałęzi, identyfikatory commitów i format dat zależą od środowiska. Lokalny commit nie wysyła danych do serwisu GitHub.

## Dokumentacja

- [Pro Git: zapisywanie zmian w repozytorium](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository).
- [Git: restore](https://git-scm.com/docs/git-restore).
- [Git: diff](https://git-scm.com/docs/git-diff).
- [Git: gitignore](https://git-scm.com/docs/gitignore).

Dostęp: 4 listopada 2026 r. Polecenia i przykłady przygotowano dla tej lekcji.
