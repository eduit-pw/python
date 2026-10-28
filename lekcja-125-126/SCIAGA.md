# Temat 61. Docker: polecenia i pliki

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `FROM python:3.13-slim` | Baza obrazu | Wybierz linię zgodną z projektem. |
| `WORKDIR /app` | Katalog roboczy w obrazie | Kolejne polecenia używają tej lokalizacji. |
| `COPY requirements.txt .` | Kopiowanie plików do obrazu | Osobna warstwa ułatwia wykorzystanie cache. |
| `RUN python -m pip install -r requirements.txt` | Instalacja zależności | Wykonywana przy budowaniu. |
| `CMD ["python", "-m", "uvicorn", ...]` | Domyślny start kontenera | Lista argumentów w formacie JSON. |
| `docker build -t pokaz-api .` | Budowanie obrazu | Kropka oznacza kontekst bieżącego folderu. |
| `docker run --rm -p 8000:8000 pokaz-api` | Start i mapowanie portu | Lewy port hosta, prawy kontenera. |
| `-v pokaz-dane:/app/dane` | Nazwany wolumen | Dane poza jednorazową warstwą kontenera. |
| `docker logs nazwa` | Odczyt logów | Użyj nazwy lub ID kontenera. |

## Krótki wzorzec

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Wzorzec Dockerfile wymaga main.py i requirements.txt zawierającego FastAPI oraz Uvicorn. Dodaj .dockerignore wykluczający .venv, .git, .env i pliki robocze. Samo EXPOSE nie publikuje portu.

[Dokumentacja](https://docs.docker.com/reference/dockerfile/) · [Zadania lekcji](README.md)
