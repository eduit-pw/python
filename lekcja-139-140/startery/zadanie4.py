# Temat 70. Zadanie 4. Dla chętnych: Blokujące i nieblokujące oczekiwanie
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: W dwóch zadaniach porównaj time.sleep(0.3) z await asyncio.sleep(0.3).
# TODO: W obu wariantach zaplanuj zadania współbieżnie i zmierz czas.
# TODO: Wyjaśnij, dlaczego time.sleep blokuje postęp drugiego zadania.

import asyncio
import time
from time import perf_counter

async def czekaj(blokujaco):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

async def blokowanie():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
