from pathlib import Path
def przygotuj(katalog):
    cel = Path(katalog) / "raporty" / "2026"
    cel.mkdir()
    return cel
