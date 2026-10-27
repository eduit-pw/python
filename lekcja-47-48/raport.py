def zapisz_wynik(bufor, nazwa, czy_ok):
    """Zapisuje wiersz dla napisu nazwa i wartości logicznej czy_ok."""
    if czy_ok:
        tekst = nazwa + ": OK\n"
    else:
        tekst = nazwa + ": FAIL\n"
    bufor.write(tekst)
