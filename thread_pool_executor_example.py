import time
from concurrent.futures import ThreadPoolExecutor


def task(n):
    time.sleep(1)
    return n


start = time.time()

with ThreadPoolExecutor(max_workers=3) as ex:
    results = list(ex.map(task, range(6)))

print("results:", results)
print("time:", time.time() - start)
