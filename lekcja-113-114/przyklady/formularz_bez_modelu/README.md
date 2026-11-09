# Formularz bez modelu

Przykład do końcowej części tematu 57. Dwa pola `forms.IntegerField` mają zakres 0–100. Formularz korzysta z funkcji `pomnoz()` w osobnym module. Sprawdź 7 i 2, zero oraz wartość -1.

Pracuj w kopii tego folderu. Użyj aktywnego środowiska z Django 5.2.x. Z folderu `manage.py` uruchom:

```text
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Otwórz http://127.0.0.1:8000/ . Przy błędzie formularz pokazuje komunikat i zachowuje wpis. Wynik 0 także pozostaje widoczny. Dane obliczeń nie są zapisywane w bazie.
