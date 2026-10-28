# Temat 01. Uruchamianie i środowisko

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `py --version` | Odczyt wersji Pythona | Polecenie terminalu Windows. |
| `py plik.py` | Wykonanie zapisanego skryptu | Uruchom w folderze pliku albo podaj ścieżkę. |
| `py -m venv .venv` | Utworzenie środowiska projektu | Własny kod zapisuj obok .venv. |
| `.\.venv\Scripts\Activate.ps1` | Aktywacja w PowerShell | Dotyczy bieżącego terminalu. |
| `.\.venv\Scripts\python.exe plik.py` | Wykonanie bez aktywacji | Używa interpretera z tego środowiska. |
| `python -m pip install nazwa` | Instalacja do wybranego interpretera | Wykonuj po wyborze właściwego środowiska. |
| `print("Cześć")` | Wyświetlenie napisu w Pythonie | Domyślnie kończy wiersz. |
| `# komentarz` | Opis w pliku .py | Interpreter pomija treść komentarza. |

## Krótki wzorzec

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe pokaz.py
```

Polecenia z tego przykładu wpisuj w PowerShell. Plik pokaz.py utwórz wcześniej, np. z instrukcją print("Cześć"). Znak >>> oznacza tryb interaktywny Pythona. Środowisko na nowym komputerze odtwórz, zamiast kopiować .venv.

[Dokumentacja](https://docs.python.org/3.13/library/venv.html) · [Zadania lekcji](README.md)
