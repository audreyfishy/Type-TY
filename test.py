import asyncio
import time

class Test:
    x = 0
    def __init__(self, id):
        self.loop = asyncio.new_event_loop()
        self.id = id
    def __del__(self):
        self.loop.close()
    def doTest(self):
        self.loop.run_until_complete(self.test())
    async def test(self):
        for _ in range(2):
            print(time.time(), end='')
            print(" " + self.id)
            self.x += 1
            await asyncio.sleep(1)

test = Test("fwa")
test.doTest()
t = Test("odoritora")
t.doTest()
test.doTest()
print(test.x, t.x)