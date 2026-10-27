# Temat 54. Wyjaśnienia do praktyki

## Panel administratora

Rejestracja modelu udostępnia go w panelu admina. createsuperuser tworzy konto lokalne. Admin i własny widok pracują na tych samych rekordach modelu.

## ModelForm

ModelForm wiąże formularz z modelem i wybranymi polami. Dla POST przekaż request.POST. is_valid wykonuje walidację i udostępnia cleaned_data albo błędy.

## GET i POST

GET pokazuje pusty formularz. POST sprawdza dane i zapisuje tylko poprawne. Przy błędzie pokaż ten sam formularz z danymi i komunikatami.

## Przekierowanie

Po zapisie przekieruj do listy. Odświeżenie strony docelowej nie powinno ponownie wysłać wcześniejszego POST i utworzyć duplikatu.

## CSRF

csrf_token w formularzu współpracuje z middleware. Brak wymaganego tokenu w POST może dać 403. Nie wyłączaj ochrony po to, aby ukryć błąd konfiguracji formularza.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
