# Temat 19. Wyjaśnienia do praktyki

## Polimorfizm

Ta sama operacja obj.pole() może działać inaczej dla prostokąta i trójkąta. Wspólna pętla korzysta z interfejsu bez sprawdzania typu każdego obiektu.

## Duck typing

Python może obsługiwać różne obiekty o zgodnym zachowaniu także bez wspólnej bazy. Ważne, aby używana metoda istniała i miała odpowiedni kontrakt.

## ABC i metoda abstrakcyjna

Dziedziczenie po ABC i @abstractmethod jawnie określa wymagania. Nie utworzysz instancji klasy z niezaimplementowanymi metodami abstrakcyjnymi.

## Kontrakt metody

Jeśli pole ma zwracać liczbę, wszystkie figury muszą zwracać liczbę. Sam print daje None i uniemożliwia sumowanie. Zachowaj sposób wywołania metody w podklasach.

## Normalizacja odpowiedzi

strip usuwa skrajne białe znaki, lower lub upper ujednolica litery. Nie usuwaj spacji wewnętrznych, gdy polecenie wymaga dokładnego tekstu. Sprawdź puste i niedozwolone odpowiedzi.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
