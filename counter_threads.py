import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count


def count(n: int) -> None:
    while n > 0:
        n -= 1
        
total = 100_000_000
workers = 8
chunk = total // workers
parts = [chunk] * workers
parts[0] += total - chunk * workers

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=workers) as ex:
    list(ex.map(count, parts))
stop = time.perf_counter()
print(f"Time spent threads: {stop - start}")
