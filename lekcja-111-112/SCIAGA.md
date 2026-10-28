# Temat 54. Django: admin i formularze

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `python manage.py createsuperuser` | Konto administratora | Wymaga przygotowanej bazy. |
| `admin.site.register(Model)` | Rejestracja modelu w panelu | Zwykle w admin.py. |
| `class Formularz(forms.Form):` | Formularz niezależny od modelu | Definiuje pola i walidację. |
| `class Formularz(forms.ModelForm):` | Formularz powiązany z modelem | Meta wskazuje model i dozwolone fields. |
| `Formularz(request.POST)` | Formularz z przesłanymi danymi | Nie oznacza jeszcze, że dane są poprawne. |
| `formularz.is_valid()` | Uruchomienie walidacji | Wynik bool. |
| `formularz.cleaned_data` | Dane po walidacji | Korzystaj po udanym is_valid(). |
| `formularz.save()` | Zapis ModelForm | Nie występuje w zwykłym Form. |
| `{% csrf_token %}` | Token w formularzu POST | Zachowaj ochronę CSRF. |

## Krótki wzorzec

```python
from django import forms

class FormularzKoloru(forms.Form):
    nazwa = forms.CharField(max_length=40)

formularz = FormularzKoloru({"nazwa": "  zielony  "})
if formularz.is_valid():
    print(formularz.cleaned_data["nazwa"])  # zielony
```

Przykład uruchom w skonfigurowanym projekcie Django. request.POST zawiera dane wejściowe, a cleaned_data dane po walidacji i konwersji.

[Dokumentacja](https://docs.djangoproject.com/en/5.2/topics/forms/) · [Zadania lekcji](README.md)
