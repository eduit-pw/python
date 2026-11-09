from django import forms


class ObliczeniaForm(forms.Form):
    liczba = forms.IntegerField(label="Liczba", min_value=0, max_value=100)
    mnoznik = forms.IntegerField(label="Mnożnik", min_value=0, max_value=100)
