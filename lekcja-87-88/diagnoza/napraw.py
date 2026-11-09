def szukaj(dane, cel):
    lewy, prawy = 0, len(dane) - 1
    while lewy < prawy:
        srodek = (lewy + prawy) // 2
        if dane[srodek] == cel:
            return srodek
        if dane[srodek] < cel:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1
