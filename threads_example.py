import threading

counter = 0
lock = threading.Lock()


def worker(n):
    global counter
    for _ in range(n):
        with lock:

            counter += 1  # ❌ race condition


threads = [threading.Thread(target=worker, args=(2,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("counter =", counter)  # quase sempre < 1_600_000
