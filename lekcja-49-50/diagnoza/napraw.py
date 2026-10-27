def podwoj_wynik(funkcja):
    def opakowanie(*args, **kwargs):
        funkcja(*args, **kwargs) * 2
    return opakowanie
@podwoj_wynik
def suma(a, b):
    return a + b
