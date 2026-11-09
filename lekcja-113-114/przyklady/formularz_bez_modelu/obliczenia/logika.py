def pomnoz(liczba: int, mnoznik: int) -> int:
    """Cel: obliczenie wyniku z dwóch liczb.

    liczba, mnoznik: liczby całkowite 0–100.
    Zwraca: int, iloczyn argumentów.
    """
    if not 0 <= liczba <= 100 or not 0 <= mnoznik <= 100:
        raise ValueError("Obie liczby muszą należeć do zakresu 0–100")
    return liczba * mnoznik
