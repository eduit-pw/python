def ostatni_element(wartosci):
    if not wartosci:
        raise ValueError("Lista nie może być pusta.")
    return wartosci[len(wartosci)]


if __name__ == "__main__":
    print(ostatni_element([4, 7, 9]))
