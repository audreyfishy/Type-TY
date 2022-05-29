import asyncio

async def f():
    return 100

asyncio.send(f)