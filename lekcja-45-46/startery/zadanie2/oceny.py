class OcenaError(ValueError):
    pass

def sprawdz_ocene(ocena):
    if type(ocena) is not int:
        raise TypeError("Ocena musi być typu int.")
    if ocena < 1 or ocena > 6:
        raise OcenaError("Zakres: 1-6.")
    return ocena
