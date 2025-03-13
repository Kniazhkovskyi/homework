def cache(func):
    cache_storage = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in cache_storage:
            print("Using cached result")
            return cache_storage[key]

        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result

    return wrapper


import time

@cache
def slow_function(x):
    time.sleep(2)
    return x * x

print(slow_function(4))  # Первый вызов, долго
print(slow_function(4))  # Второй вызов, быстро из кэша