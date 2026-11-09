from django.shortcuts import render
from .forms import ObliczeniaForm
from .logika import pomnoz


def formularz(request):
    form = ObliczeniaForm(
        request.POST if request.method == "POST" else None)
    wynik = None
    if request.method == "POST" and form.is_valid():
        wynik = pomnoz(form.cleaned_data["liczba"],
                     form.cleaned_data["mnoznik"])
    return render(request, "obliczenia/formularz.html",
                  {"form": form, "wynik": wynik})
