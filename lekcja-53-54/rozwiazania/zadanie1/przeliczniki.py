def minuty_na_sekundy(minuty):
    return minuty * 60


def opis_czasu(minuty):
    return f"{minuty} min = {minuty_na_sekundy(minuty)} s"
