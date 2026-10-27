from django import forms
class Formularz(forms.Form):
    imie = forms.CharField(min_length=2)
def sprawdz(dane):
    formularz = Formularz(dane)
    return bool(formularz.is_valid)
