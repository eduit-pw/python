# Parametry polecenia uruchomienia Uvicorn wewnątrz kontenera.
def argumenty():
    return ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
