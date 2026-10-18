def szyfruj(tekst, klucz):
    """Szyfruje małe litery a-z i zachowuje spacje; klucz jest int."""
    wynik = ""
    for znak in tekst:
        if znak == " ":
            wynik = wynik + " "
        else:
            indeks = ord(znak) - ord("a")
            nowy = (indeks + klucz) % 26
            litera = chr(ord("a") + nowy)
            wynik = wynik + litera
    return wynik

def main():
    tekst = input("Tekst (male litery i spacje): ")
    klucz = int(input("Klucz: "))
    print(szyfruj(tekst, klucz))

if __name__ == "__main__":
    main()
