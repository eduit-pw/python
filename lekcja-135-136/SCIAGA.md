# Temat 65. logging

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `logging.getLogger(__name__)` | Logger modułu | Nazwa pomaga znaleźć źródło wpisu. |
| `logging.basicConfig(...)` | Podstawowa konfiguracja | Zwykle raz, w punkcie wejścia programu. |
| `level=logging.INFO` | Próg komunikatów | DEBUG poniżej progu nie zostanie zapisany. |
| `DEBUG, INFO, WARNING, ERROR, CRITICAL` | Poziomy rosnącej ważności | Najniższy: DEBUG. |
| `logger.info("Liczba: %s", n)` | Wpis z argumentami | Formatowanie zostaje obsłużone przez logging. |
| `logger.exception("Opis")` | Wpis ERROR ze stosem wyjątku | Używaj wewnątrz except. |
| `filename="app.log", encoding="utf-8"` | Zapis do pliku | Domyślny filemode to dopisywanie "a". |
| `%(asctime)s, %(levelname)s, %(message)s` | Pola formatu | Np. data, poziom, komunikat. |

## Krótki wzorzec

```python
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)
logger.debug("Ten wpis jest poniżej progu")
logger.info("Przetworzono %s pliki", 3)
# INFO: Przetworzono 3 pliki
```

Logger i jego handlery mogą mieć osobne progi. Duplikaty wpisów mogą wynikać z wielu handlerów albo propagacji do loggera nadrzędnego.

[Dokumentacja](https://docs.python.org/3.13/howto/logging.html) · [Zadania lekcji](README.md)
