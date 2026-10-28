# Temat 52. Django: szablony

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `render(request, "strony/widok.html", kontekst)` | Renderowanie HTML | Zwraca HttpResponse. |
| `{"nazwa": wartosc}` | Kontekst szablonu | Klucze stają się nazwami w HTML. |
| `{{ nazwa }}` | Wstawienie wartości | Django domyślnie stosuje escapowanie HTML. |
| `{% if warunek %} ... {% endif %}` | Warunek w szablonie | Nie jest składnią if Pythona. |
| `{% for x in dane %} ... {% empty %} ... {% endfor %}` | Pętla i przypadek pustych danych | empty jest opcjonalne. |
| `{{ nazwa\|length }}` | Filtr długości | Zapis z pionową kreską należy do składni szablonu. |
| `{% url 'nazwa' %}` | Adres na podstawie nazwy trasy | Unika wpisywania ścieżki na sztywno. |
| `templates/strony/widok.html` | Typowe miejsce pliku | W aplikacji obecnej w INSTALLED_APPS przy APP_DIRS=True. |

## Krótki wzorzec

```html
<h1>{{ tytul }}</h1>
<ul>
{% for kolor in kolory %}
  <li>{{ kolor }}</li>
{% empty %}
  <li>Brak kolorów</li>
{% endfor %}
</ul>
```

Przykład to szablon HTML, któremu widok przekazuje tytul oraz kolory. Nie dodawaj filtra safe do niezweryfikowanego tekstu użytkownika.

[Dokumentacja](https://docs.djangoproject.com/en/5.2/topics/templates/) · [Zadania lekcji](README.md)
