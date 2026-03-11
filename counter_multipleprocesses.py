import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count


def count(n: int) -> None:
    while n > 0:
        n -= 1
        
def main():
    total = 100_000_000
    workers = cpu_count()
    chunk = total // workers
    parts = [chunk] * workers
    parts[0] += total - chunk * workers

    start = time.perf_counter()
    with Pool(processes=workers) as p:
        p.map(count, parts)
    stop = time.perf_counter()
    print(f"Time spent multiprocessing: {stop - start}")
    print(f"Number of workers: {workers}")

if __name__ == "__main__":
    main()
