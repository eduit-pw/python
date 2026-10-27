# Temat 16. Wyjaśnienia do praktyki

## __str__

str(obj) i print(obj) korzystają z __str__. Metoda zwraca str z opisem dla użytkownika. Nie umieszczaj w niej samego print, bo jego wynik None nie spełnia kontraktu.

## __repr__

repr(obj) daje reprezentację do analizy. Lista obiektów używa repr swoich elementów. !r we f-stringu również pobiera repr i poprawnie reprezentuje argument napisowy.

## __len__

len(obj) wywołuje __len__, które ma zwrócić nieujemny int. Dla własnej kolekcji zwykle zwracasz długość jej listy wewnętrznej, także 0.

## __eq__ i is

== korzysta z porównania wartości, które możesz zdefiniować w __eq__. is sprawdza tożsamość. Równe współrzędne nie oznaczają tego samego obiektu.

## NotImplemented

Dla nieobsługiwanego typu argumentu __eq__ może zwrócić NotImplemented. Jest to specjalna wartość, a nie wyjątek NotImplementedError. Python może wtedy spróbować drugiego porównania.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
