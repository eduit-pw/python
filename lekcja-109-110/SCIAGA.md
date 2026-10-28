# Temat 53. Django ORM i migracje

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `class Rekord(models.Model):` | Model danych | Klasa zapisana zwykle w models.py. |
| `models.CharField(max_length=80)` | Krótkie pole tekstowe | Długość określ jawnie. |
| `models.IntegerField(), models.BooleanField(default=False)` | Liczba i flaga | Typy kolumn modelu. |
| `python manage.py makemigrations` | Przygotowanie migracji | Zapisuje zmianę schematu w pliku. |
| `python manage.py migrate` | Zastosowanie migracji | Wykonuje zmiany w bazie. |
| `Model.objects.create(pole=wartosc)` | Utworzenie i zapis | Zwraca obiekt modelu. |
| `Model.objects.filter(pole=wartosc)` | Filtrowanie | Zwraca QuerySet, który może być pusty. |
| `Model.objects.get(pk=id)` | Jeden obiekt | Może zgłosić DoesNotExist lub MultipleObjectsReturned. |
| `obj.save(), obj.delete()` | Zapis zmian i usunięcie | Zmiana pola w Pythonie sama nie aktualizuje bazy. |

## Krótki wzorzec

```python
# models.py istniejącej aplikacji Django
from django.db import models

class Kolor(models.Model):
    nazwa = models.CharField(max_length=40)
    aktywny = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa
```

Po zmianie modelu przygotuj i zastosuj migrację. Pliki migracji dodawaj do repozytorium. ORM nie usuwa potrzeby walidacji reguł biznesowych.

[Dokumentacja](https://docs.djangoproject.com/en/5.2/topics/db/models/) · [Zadania lekcji](README.md)
