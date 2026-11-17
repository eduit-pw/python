import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def pobierz_status(url="http://127.0.0.1:8000/status"):
    with urlopen(url, timeout=5) as odpowiedz:
        dane = json.loads(odpowiedz.read().decode("utf-8"))
    if not isinstance(dane, dict) or dane.get("stan") != "ok":
        raise ValueError("Niepoprawna struktura odpowiedzi")
    return dane


if __name__ == "__main__":
    try:
        print(pobierz_status())
    except HTTPError as blad:
        print(f"Błąd HTTP: {blad.code}")
    except URLError as blad:
        print(f"Brak połączenia: {blad.reason}")
    except (ValueError, UnicodeError) as blad:
        print(f"Błędne dane: {blad}")
