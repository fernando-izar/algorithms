import asyncio
import time


async def delay_1():
    await asyncio.sleep(1)
    print("One second")
    return "One second"


async def delay_5():
    await asyncio.sleep(5)
    print("Five seconds")
    return "Five seconds"


async def delay_2():
    await asyncio.sleep(2)
    print("Two seconds")
    return "Two seconds"


async def main():
    # task5 = asyncio.create_task(delay_5())
    # task1 = asyncio.create_task(delay_1())
    # task2 = asyncio.create_task(delay_2())

    # await task1
    # await task5

    results = await asyncio.gather(delay_2(), delay_1(), delay_5())
    print(results)


asyncio.run(main())
