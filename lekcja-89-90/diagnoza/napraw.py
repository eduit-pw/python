from pathlib import Path
def zapisz(nazwa, tekst):
    Path(nazwa).write_text(tekst, encoding="utf-8")
    return True
