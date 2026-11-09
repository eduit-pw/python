def srednia(wartosci):
    if not wartosci:
        raise ValueError("Lista nie może być pusta.")
    return sum(wartosci) // len(wartosci)


if __name__ == "__main__":
    print(srednia([2, 3]))
