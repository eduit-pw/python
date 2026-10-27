# Temat 52. Wyjaśnienia do praktyki

## Kontekst szablonu

render(request, szablon, kontekst) buduje odpowiedź HTML. Słownik kontekstu wiąże nazwy z danymi. {{ nazwa }} wyświetla wartość przekazaną pod danym kluczem.

## Pętla i pusty wynik

{% for x in dane %} tworzy fragment dla każdego elementu. {% empty %} działa przy braku elementów. forloop.counter daje numerowanie od 1.

## Dziedziczenie HTML

base.html przechowuje wspólny dokument i bloki. extends wybiera bazę, block wypełnia miejsce podstrony. Zmiana wspólnego nagłówka ma działać na wszystkich podstronach.

## Nazwany URL

{% url "nazwa" %} buduje odnośnik według konfiguracji. Nazwa trasy i adres tekstowy nie są tym samym. Unikaj ręcznego powtarzania ścieżek w wielu szablonach.

## Escaping

Domyślnie Django zamienia specjalne znaki HTML w bezpieczny tekst. <b> wpisane jako dane ma być widoczne dosłownie. safe i wyłączenie autoescape zmieniają to zachowanie.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
