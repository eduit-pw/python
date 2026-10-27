def liczba(tekst):
    try:
        return int(tekst)
    except TypeError:
        return None
