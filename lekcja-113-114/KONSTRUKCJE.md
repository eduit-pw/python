# Temat 57. Django: admin i formularze

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

## Utrwalanie Git w ramach tego bloku

Przed zmianą sprawdź `git status`, a po działającej poprawce obejrzyj `git diff`. Zapisz mały commit z opisem wykonanej zmiany. Czynność zajmuje 2–3 minuty przewidziane na sprawdzenie pracy.

## Formularz bez modelu

| Konstrukcja | Użycie |
| --- | --- |
| `class MnozenieForm(forms.Form)` | Formularz niepowiązany z modelem bazy. |
| `forms.IntegerField(min_value=0, max_value=100)` | Liczba całkowita z ustalonego zakresu. |
| `form.cleaned_data["liczba"]` | Odczyt danych po poprawnym is_valid(). |
| `{% if wynik is not None %}` | Pokazanie również wyniku 0. |

