import time


def count(n: int) -> None:
    while n > 0:
        n -= 1
    

start = time.perf_counter()
count(100_000_000)
stop = time.perf_counter()

print(f"Time spent: {stop - start}")
        
    