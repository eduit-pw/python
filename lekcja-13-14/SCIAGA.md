# Temat 7. Wyjaśnienia do praktyki

## Zakres nazw

Nazwa przypisana w funkcji jest zwykle lokalna. Python szuka nazw kolejno w zakresie lokalnym, otaczającym, module i wbudowanych. Lokalna nazwa może przesłonić zewnętrzną.

## Wartość domyślna

Domyślny argument pozwala pominąć wartość w wywołaniu. Obiekt domyślny powstaje przy definicji funkcji. Lista [] jako wartość domyślna może przez to zbierać dane z wielu wywołań.

## None i nowa lista

Użyj tagi=None i utwórz nową listę, gdy tagi is None. Lista przekazana jawnie nadal jest tym samym obiektem. Wzorzec None nie kopiuje argumentu.

## *args i **kwargs

*args zbiera dodatkowe argumenty pozycyjne do krotki. **kwargs zbiera nazwane do słownika. Nazwy args i kwargs są umowne, gwiazdki określają zachowanie.

## Argumenty tylko nazwane

Parametry po samodzielnej * albo po *args podawaj po nazwie. Zapis premia=3 wyjaśnia znaczenie liczby. Nie zastępuj komunikacji argumentami przez modyfikację zmiennych globalnych.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
