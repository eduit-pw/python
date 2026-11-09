class Notatka:
    def __init__(self, tekst):
        tekst = tekst.strip()
        if not tekst:
            raise ValueError("Treść notatki nie może być pusta.")
        self.tekst = tekst

    def __str__(self):
        return self.tekst
