from rabaty import cena_po_rabacie


def main():
    proby = [(20000, 15), (20000, 0), (20000, 100)]
    for cena_grosze, procent in proby:
        wynik = cena_po_rabacie(cena_grosze, procent)
        print(cena_grosze, procent, wynik)


if __name__ == "__main__":
    main()
