import json
def suma_json(tekst):
    dane = json.dumps(tekst)
    return sum(dane["liczby"])
