def cached(max_size=3):
    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(*args):
            if args in cache:
                return cache[args]

            result = func(*args)
            cache[args] = result

            if len(cache) > max_size:
                # Remove the first cached item (FIFO strategy)
                next(iter(cache))
                del cache[next(iter(cache))]

            return result

        return wrapper

    return decorator


@my_cached(max_size=3)
def func(a: str, b: str) -> str:
    print("func called")
    return a + b


print(func("a", "b"))  # "func called", "ab"
print(func("a", "b"))  # "ab"
print(func("a", "c"))  # "func called", "ac"
print(func("a", "d"))  # "func called", "ad"
print(func("a", "b"))  # "func called", "ab"


from functools import wraps
