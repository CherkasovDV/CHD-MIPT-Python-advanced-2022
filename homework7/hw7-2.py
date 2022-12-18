import time
from functools import lru_cache

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        return time.time() - start_time
    return wrapper

def fib(count):
    if count == 1 or count == 2:
        return 1
    else:
        return fib(count - 1) + fib(count - 2)

@time_decorator
def fib_time(count):
    return fib(count)

@time_decorator
def fib_cycle_time(count):
    fib1 = fib2 = 1
    for _ in range(2, count):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2

@lru_cache(maxsize=None)
def fib_lru(count):
    if count == 1 or count == 2:
        return 1
    else:
        return fib_lru(count - 1) + fib_lru(count - 2)

@time_decorator
def fib_lru_time(count):
    return fib_lru(count)

a = 40
print("Однократное вычисление 40-ого числа Фибоначчи рекурсией. Время: ", fib_time(a))
b = 400
lru = 0
cycle = 0
for i in range(1000):
    lru += fib_lru_time(b)
    cycle += fib_cycle_time(b)
print("Тысячакратное вычисление 400-ого числа Фибоначчи с лру-кэшированием. Время: ", lru)
print("Тысячакратное вычисление 400-ого числа Фибоначчи циклами. Время: ", cycle)
if cycle > lru:
    print("Lru works faster.")
elif cycle < lru:
    print("Cycle works faster.")
else:
    print("Cannot be identified. Please increase range")
