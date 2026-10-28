# Temat 48. Pakowanie programu

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `python -m PyInstaller main.py` | Budowanie aplikacji | Polecenie terminalu w środowisku projektu. |
| `--onedir` | Folder z programem i zależnościami | Łatwiejszy do sprawdzenia przy pierwszej próbie. |
| `--onefile` | Jeden plik uruchomieniowy | Zasoby rozpakowuje podczas startu. |
| `--windowed` | Uruchamianie GUI bez konsoli na Windows | Przy błędach zacznij od wariantu z konsolą. |
| `--name Nazwa` | Nazwa wyniku | Np. --name Pokaz. |
| `--add-data "okno.ui:."` | Dołączenie zasobu | Składnia zgodna z PyInstaller 6. |
| `dist/` | Wynik budowania | Przekaż pełną zawartość wymaganą przez wybrany wariant. |
| `build/, plik.spec` | Pliki procesu budowania | .spec opisuje konfigurację pakowania. |

## Krótki wzorzec

```powershell
python -m PyInstaller --clean --onedir --name Pokaz main.py
python -m PyInstaller --clean --onedir --add-data "okno.ui:." main.py
```

Polecenia są alternatywnymi przykładami i wymagają istniejących main.py oraz, w drugim przypadku, okno.ui. Buduj na systemie docelowym. Dane użytkownika zapisuj poza tymczasowo rozpakowanymi zasobami. Sprawdź program na osobnym stanowisku.

[Dokumentacja](https://pyinstaller.org/en/v6.16.0/usage.html) · [Zadania lekcji](README.md)
