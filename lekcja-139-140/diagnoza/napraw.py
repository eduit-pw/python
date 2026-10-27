import asyncio
async def praca(x):
    await asyncio.sleep(0)
    return x * 2
async def wszystkie(dane):
    return [praca(x) for x in dane]
