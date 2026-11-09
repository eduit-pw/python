from notatki.logika import Notatnik


def main():
    notatnik = Notatnik()
    while True:
        print("1. Dodaj notatkę  2. Pokaż notatki  0. Koniec")
        opcja = input("Opcja: ").strip()
        if opcja == "0":
            break
        if opcja == "1":
            try:
                notatka = notatnik.dodaj(input("Treść: "))
                print(f"Dodano: {notatka}")
            except ValueError as blad:
                print(blad)
        elif opcja == "2":
            notatki = notatnik.wszystkie()
            if not notatki:
                print("Brak notatek.")
            for numer, notatka in enumerate(notatki, 1):
                print(f"{numer}. {notatka}")
        else:
            print("Nieznana opcja.")


if __name__ == "__main__":
    main()
