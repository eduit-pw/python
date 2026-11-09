def cena_po_rabacie(cena_grosze, procent):
    if cena_grosze < 0:
        raise ValueError("Cena nie może być ujemna.")
    if procent < 0 or procent > 100:
        raise ValueError("Rabat musi należeć do zakresu 0–100.")
    rabat = cena_grosze * procent // 100
    wynik = cena_grosze - rabat
    return wynik


if __name__ == "__main__":
    print(cena_po_rabacie(20000, 15))
