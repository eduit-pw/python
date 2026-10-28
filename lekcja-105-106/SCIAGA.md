# Temat 51. Django: projekt, adres i widok

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `python -m django startproject config .` | Utworzenie projektu w bieżącym folderze | Powstaje manage.py i pakiet config. |
| `python manage.py startapp strony` | Utworzenie aplikacji | Dodaj ją do INSTALLED_APPS, gdy korzystasz z jej zasobów. |
| `python manage.py runserver` | Serwer deweloperski | Domyślnie http://127.0.0.1:8000. |
| `path("adres/", widok, name="nazwa")` | Reguła adresu | Import path z django.urls. |
| `path("liczba/<int:n>/", widok)` | Parametr ścieżki | Do widoku trafi int pod nazwą n. |
| `include("strony.urls")` | Dołączenie tras aplikacji | Adres końcowy składa się z prefiksu i trasy aplikacji. |
| `def widok(request):` | Funkcja obsługująca żądanie | Musi zwrócić odpowiedź HTTP. |
| `HttpResponse("tekst")` | Prosta odpowiedź | Import z django.http. |

## Krótki wzorzec

```python
# views.py
from django.http import HttpResponse

def witaj(request):
    return HttpResponse("Dzień dobry")

# W urls.py tej samej aplikacji:
from django.urls import path
urlpatterns = [path("witaj/", witaj, name="witaj")]
```

To wzorzec do projektu Django. Gdy urlpatterns jest w osobnym pliku urls.py, zaimportuj witaj przez from .views import witaj. Serwer runserver służy do pracy lokalnej.

[Dokumentacja](https://docs.djangoproject.com/en/5.2/intro/tutorial01/) · [Zadania lekcji](README.md)
